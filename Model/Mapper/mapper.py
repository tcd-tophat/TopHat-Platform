import abc
#import config
import database
import mappererror
import objectwatcher as OW
import domainobject
import collection
import identityobject

import inspect

class Mapper:
	__metaclass__ = abc.ABCMeta
	db = None

	def __init__(self):
		try:
			#cnf = config.getConfig()
			#self.db = database.Database(cnf.MySQLHost, cnf.MySQLUser, cnf.MySQLPass, cnf.MySQLDatabase)
			self.db = database.Database("localhost", "root", "root", "tophat")
		except KeyError:
			raise NameError("Cannot load database details from the config file")

	def find(self, id_):
		"""Gets the object for that database id"""

		# check not already in watcher's list if so return that instance - no need to query the DB then
		old = self.getFromWatcher(id_)
		if old:
			return old

		# check memcache

		# gonna have to load object off the disk (database server)
		query = self._selectStmt()
		parameters = id_,

		cursor = self.db.getCursor()
		rowsAffected = cursor.execute(query, parameters)	# bind the id to the query and run it
		data = cursor.fetchone()							# fetch the one row from the DB
		cursor.close()

		if rowsAffected > 0:								# if a row was returned then build and object from it
			return self.createObject(data)
		else:
			return None

	def createObject(self, data):
		"""Turns results from the database into objects that the rest of the program understands"""
		# Check if we have made this object before - no need to make it twice
		old = self.getFromWatcher(data["id"])
		if old is not None:
			return old

		# it does not exist create object
		obj = self._doCreateObject(data)

		obj.markClean()	# new objects are always clean

		# add new object to the watcher's list
		if obj is not None:
			self.addToWatcher(obj)

		return obj

	def findAll(self, start = 0, number = 50):
		"""Finds all the objects in such a table from start to (start + number)"""
		# check that the limit params are not off the wall
		if start < 0:
			print "The start point must be a positive int"
			start = 0

		if number > 50:
			print "You cannot select more than 50 rows at one time"
			number = 50

		# build the query
		query = self._selectAllStmt()
		params = (start, start + number)

		# run the qurery
		cursor = self.db.getCursor()
		rowsAffected = cursor.execute(query, params)
		data = cursor.fetchall()
		cursor.close()

		if rowsAffected > 0:								# check if there are results to be returned
			return collection.Collection(data, self) 		# create a collection object for the results
		else:
			return None

	def delete(self, obj):
		"""Deletes a given object from the database"""
		if not isinstance(obj, domainobject.DomainObject):
			raise mappererror.MapperError("This function expects a DomainObject object as the input parameter")

		if obj.getid() is -1:
			raise mappererror.MapperError("You cannot delete an object that was never in the database. It has no id")

		print "Deleting new " + str(type(obj)) + " object " + str(obj.getId())

		return self._doDelete(obj)				


	def update(self, obj):
		"""Updates a given object's records in the database"""
		if not isinstance(obj, domainobject.DomainObject) :
			raise mappererror.MapperError("This function expects a DomainObject object as the input parameter")

		if obj.getId() is -1:		# can't update an object that has not been inserted
			raise mappererror.MapperError("You can only update objects that are in the database, please insert this object first")

		print "Update new " + str(type(obj)) + " object " + str(obj.getId())

		return self._doUpdate(obj)


	def insert(self, obj):
		"""Inserts this object into the database as its records"""
		if not isinstance(obj, domainobject.DomainObject):
			raise mappererror.MapperError("This function expects a DomainObject object as the input parameter")

		print "Inserting new " + str(type(obj)) + " object " + str(obj.getId())

		result = self._doInsert(obj)					# do the insertion specifics

		if result:
			self.addToWatcher(obj)							# add the new object to the object watcher

		return result

	def selectIdentity(self, identityObj, limitStart = 0, limitDistance = 50):
		"""Builds a dynamic query using the identityObject to collect the parameters"""

		# check we get an instance of identityObject
		if not isinstance(identityObj, identityobject.IdentityObject):
			raise mappererror.MapperError("Must pass in an identityObject")

		# Check the range parameters are valid
		if limitStart < 0:
			raise mappererror.MapperError("The start point must be a positive int")

		if limitDistance > 50:
			raise mappererror.MapperError("You cannot select more than 50 rows at one time")

		if limitDistance < 1:
			raise mappererror.MapperError("You must select at least one row")

		# =======================================
		# build the query from the identityObject's data
		query = "SELECT * FROM " + self.tableName() + " WHERE "

		params = []													# create a list to store all the parameters in

		# build the WHERE clause of the query
		for field in identityObj.fields:
			first = True
			for comp in identityObj.fields[field].comps:
				if not first:
					query += " OR "											# join clauses for the same column using OR operator
				query += comp['name'] + " " + comp['operator'] + " %s"		# add placeholder for the column name and value
				params.append(comp['value'])								# add the value to a list of params
				first = False

			query += " AND "									# join clauses for different columns using AND operator

		query = query[:-5]											# remove the final AND from the query

		query += " LIMIT %s, %s"

		# finish preparing all the params
		params.append(limitStart)							# add the two limit params to the list
		params.append(limitStart + limitDistance)
		paramsTuple = tuple(params)								# convert the list of params into a tuple for the query exectuion

		#========================================
		# run the query and pull the results into a collection object
		cursor = self.db.getCursor()						# get the database cursor
		rowsAffected = cursor.execute(query, paramsTuple)	# run the query storing the number of rows affected
		data = cursor.fetchall()							# fetch the data from the server
		cursor.close()										# close the cursor to the database

		if rowsAffected > 0:								# check there were results to be returned
			return collection.Collection(data, self)		# return a collection of the objects
		else:
			return None										# otherwise return nada

	def null(self, value):
		if value is None:
			return "NULL"
		else:
			return value

	def getFromWatcher(self, id_):
		"""Checks if the ObjectWatcher has an instance for this object with the given id and returns if it it does"""
		watcher = OW._Objectwatcher()
		return watcher.exists(self.targetClass(), id_)

	def addToWatcher(self, obj):
		"""Adds the given instance of an object to the ObjectWatcher's list of objects"""
		watcher = OW._Objectwatcher()
		watcher.add(obj)

	# Abstract methods to be implemented by the concrete children of this class 
	@abc.abstractmethod
	def targetClass(self):
		pass

	@abc.abstractmethod
	def tableName(self):
		pass

	@abc.abstractmethod
	def _selectStmt(self):
		pass

	@abc.abstractmethod 
	def _selectAllStmt(self):
		pass

	@abc.abstractmethod 
	def _doUpdate(self, obj):
		pass

	@abc.abstractmethod 
	def _doDelete(self, obj):
		pass

	@abc.abstractmethod 
	def _doInsert(self, obj):
		pass

	@abc.abstractmethod 
	def _doCreateObject(self, data):
		pass