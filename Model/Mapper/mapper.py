import abc
import database
import mappererror as MapperError
import objectwatcher as OW
import DomainObject

class Mapper:
	__metaclass__ = abc.ABCMeta
	db = None

	def __init__(self):
		self.db = database.Database("localhost", "root", "root", "tophat")			# get the database access handler

	def find(self, id):
		""" Gets the object for that database id """

		# check not already in watcher's list if so return that instance 
		old = self.getFromWatcher(id)
		if old:
			return old

		# check memcache

		# gonna have to load object off the disk (database server)
		query = self._selectStmt()
		parameters = id,

		cursor = self.db.getCursor()
		rowsAffected = cursor.execute(query, parameters)	# bind the id to the query and run it
		data = cursor.fetchone()
		cursor.close()

		if rowsAffected > 0:
			return self.createObject(data)
		else:
			return None

	def createObject(self, data):
		""" Turns results from the database into objects that the rest of the program understands """
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
		""" Finds all the objects in such a table from start to (start + number) """
		if start < 0:
			print "The start point must be a positive int"
			start = 0

		if number > 50:
			print "You cannot select more than 50 rows at one time"
			number = 50

		# build the query
		query = self._selectAllStmt()
		params = (start, number)

		# run the qurery
		cursor = self.db.getCursor()
		rowsAffected = cursor.execute(query, params)
		data = cursor.fetchall()
		cursor.close()

		# create a list of objects from the results
		objects = []
		for row in data:
			objects.append(self.createObject(row))

		return objects

	def delete(self, obj):
		if isinstance(obj, DomainObject.DomainObject):
			raise MapperError.MapperError("This function expects a DomainObject object as the input parameter")

		if obj.id is -1:
			raise MapperError.MapperError("You cannot delete an object that was never in the database. It has no id")

		return self._doDelete(obj)				


	def update(self, obj):
		if not isinstance(obj, DomainObject.DomainObject) :
			raise MapperError.MapperError("This function expects a DomainObject object as the input parameter")

		if obj.id is -1:		# can't update an object that has not been inserted
			raise MapperError.MapperError("You can only update objects that are in the database, please insert this object into the database first")

		return self._doUpdate(obj)


	def insert(self, obj):
		if not isinstance(obj, DomainObject.DomainObject):
			raise MapperError.MapperError("This function expects a DomainObject object as the input parameter")

		result = self._doInsert(obj)

		self.addToWatcher(obj)							# warning I need to update the insert id to the obj somewhere

		return result


	def getFromWatcher(self, id):
		""" Checks if the ObjectWatcher has an instance for this object with the given id and returns if it it does """
		watcher = OW._Objectwatcher()
		return watcher.exists(self.targetClass(), id)

	def addToWatcher(self, obj):
		watcher = OW._Objectwatcher()
		watcher.add(obj)

	# Abstract methods to be implemented by the concrete children of this class 
	@abc.abstractmethod
	def targetClass(self):
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