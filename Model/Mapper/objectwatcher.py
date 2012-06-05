import Model.domainobject

class _Objectwatcher:
	"""Singleton class that keeps track of every instance of a DomainObject in this system"""

	_instance = None

	__objects = {}						# dictionary of all the objects in the system
	__new = []							# list of objects to be inserted into the database
	__dirty = []						# list of objects to be updated
	__delete = []						# list of objects to be deleted
	
	def __init__(self):
		pass

	# make it a singleton class	
	def __new__(cls, *args, **kwargs):
		if not cls._instance:
			cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
		return cls._instance

	def add(self, obj):
		"""Add an object to the watcher's list"""
		if isinstance(obj, Model.domainobject.DomainObject):
			key = self.getGlobalName(obj)
			self.__objects[key] = obj
		else:
			t = str(type(obj))
			raise Exception("Only DomainObjects can be stored in the ObjectWatcher's list, not " + t)

	def exists(self, classname, id_):
		"""Check if an object exists given its classname and id"""
		name = classname + "." + str(id_)
		if name in self.__objects:
			return self.__objects[name]
		else:
			return None

	def getGlobalName(self, obj) :
		"""Gets the global name of this object to be used as the key in the hash map"""
		return str(obj.__class__.__name__) + "." + str(obj.getId())

	def addNew(self, obj):
		"""Marks an object new so that it can be inserted into the database"""
		if obj not in self.__new:
			self.__new.append(obj)

	def addDelete(self, obj):
		"""Marks an old object that needs to be deleted from the database"""
		if obj.getId() != -1:
			if obj not in self.__delete:
				self.__delete.append(obj)

	def addDirty(self, obj):
		"""Marks an object that has changed and needs to be updated"""
		if obj.getId() != -1:						# check that the object has been inserted into the database so that there is actually a record to update
			if obj not in self.__dirty:
				self.__dirty.append(obj)

	def addClean(self, obj):
		"""Marks an object clean by removing it from the delete/dirty list of objects to be updated"""
		if obj in self.__dirty:
			self.__dirty.remove(obj)
		
		if obj in self.__delete:
			self.__delete.remove(obj)

	def printAll(self):
		print "##==================================="
		print "========================"
		print "## Dirty"
		for dirty in self.__dirty:
			print str(dirty) + " :: " + str(type(dirty))

		print "========================"
		print "## Clean"
		for new in self.__new:
			print str(new) + " :: " + str(type(new))

		print "========================"
		print "## Delete"
		for delete in self.__delete:
			print str(delete) + " :: " + str(type(delete))

		print "##==================================="

	def magicSaveAll(self):
		"""Loop through all the list of objects to change and make those changes in persistent storage"""

		# insert new objects
		for newObj in self.__new:
			M = newObj.mapperClass()	# gets the specific mapper this object needs to be added to storage
			if M is not None:
				M.insert(newObj)
			else:
				print "Unable to finder mapper for " + str(newObj) + " (" + str(type(newObj)) + ") . Object not being inserted."

		# update changed objects
		for changedObj in self.__dirty:
			M = changedObj.mapperClass() # get specific mapper for this object
			if M is not None:
				M.update(changedObj)
			else:
				print "Unable to finder mapper for " + str(changedObj) + ". Object not being updated."

		# delete old objects
		for delObj in self.__delete:
			if M is not None:
				M = delObj.mapperClass()
				M.delete(delObj)
			else:
				print "Unable to finder mapper for " + str(delObj) + ". Object not being deleted."

		# reset all lists to empty - don't want to repeat all of these actions again
		self.__new = []
		self.__dirty = []
		self.__delete = []