from abc import ABCMeta, abstractmethod

#import objectwatcher
#import database
#import mappererror

class Mapper:
	__metaclass__ = ABCMeta

	def __init__(self):
		pass

	def find(self, id):
		""" Gets the object for that database id """

		# check not already in watcher's list if so return that instance 
		old = getFromWatcher(id)
		if old:
			return old

		# check memcache

		# gonna have to load object off the disk (database server)
		data = database.con.query(self.selectStmt)
		obj = self.createObject(data)

		return obj

	def createObject(data):
		old = getFromWatcher(XXXXXidXXXXX)
		if old:
			return old

		# it does not exist create object
		obj = self.doCreateObject(data)

		# add new object to the watcher's list
		self.addToWatcher(obj)

		return obj


	def delete(obj):
		if isinstance(obj, DomainObject):
			raise MapperError("This function expects a DomainObject object as the input parameter")

		if obj.id == -1:
			raise MapperError("You cannot delete an object that was never in the database. It has no id")
		return self.doDelete(obj)				


	def update(obj):
		if isinstance(obj, DomainObject) is not:
			raise MapperError("This function expects a DomainObject object as the input parameter")

		if obj.id == -1		# can't update an object that has not been inserted
			raise MapperError("You can only update objects that are in the database, please insert this object into the database first")

		return self.doUpdate(obj)


	def insert(obj):
		if isinstance(obj, DomainObject) is not:
			raise MapperError("This function expects a DomainObject object as the input parameter")

		result = self.doInsert(obj)

		addToWatcher(obj)							# warning I need to update the insert id to the obj somewhere

		return result


	def getFromWatcher(self, id):
		""" Checks if the ObjectWatcher has an instance for this object with the given id and returns if it it does """
		watcher = _ObjectWatcher()
		watcher.exists(self.targetClass(), id)

	def addToWatcher(self, obj):
		watcher = _ObjectWatcher():
		watcher.add(obj)

	# Abstract methods to be implemented by the concrete children of this class 
	@abstractmethod
	def targetClass(self):
		pass

	@abstractmethod
	def selectStmt(self):
		pass

	@abstractmethod 
	def selectAllStmt(self):
		pass

	@abstractmethod 
	def doUpdate(self, obj):
		pass

	@abstractmethod 
	def doDelete(self, obj):
		pass

	@abstractmethod 
	def doInsert(self, obj):
		pass

	@abstractmethod 
	def doCreateObject(self, data):
		pass