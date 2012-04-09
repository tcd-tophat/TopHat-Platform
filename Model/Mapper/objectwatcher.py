import DomainObject

class _Objectwatcher:

	_instance = None

	objects = {}						# dictionary of all the objects in the system
	new = []							# list of objects to be inserted into the database
	dirty = []							# list of objects to be updated
	delete = []							# list of objects to be deleted
	
	def __init__(self):
		pass

	# make it a singleton class	
	def __new__(cls, *args, **kwargs):
		if not cls._instance:
			cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
		return cls._instance

	def add(self, obj):
		if isinstance(obj, DomainObject.DomainObject):
			key = self.getGlobalName(obj)
			self.objects[key] = obj
		else:
			t = str(type(obj))
			raise Exception("Only DomainObjects can be stored in the ObjectWatcher's list, not " + t)

	def exists(self, classname, id):
		name = classname + "." + str(id)
		if name in self.objects:
			return self.objects[name]
		else:
			return None

	def getGlobalName(self, obj) :
		""" Gets the global name of this object to be used as the key in the hash map """
		return str(obj.__class__.__name__) + "." + str(obj.id)

	def addNew(self, obj):
		""" Marks an object new so that it can be inserted into the database """
		if obj not in self.new:
			self.new.append(obj)

	def addDelete(self, obj):
		""" Marks an old object that needs to be deleted from the database """
		if obj.id != -1:
			if obj not in self.delete:
				self.delete.append(obj)

	def addDirty(self, obj):
		""" Marks an object that has changed and needs to be updated """
		if obj.id != -1:
			if obj not in self.dirty:
				self.dirty.append(obj)

	def addClean(self, obj):
		""" Marks an object clean by removing it from the delete/dirty list of objects to be updated """
		if obj in self.dirty:
			self.dirty.remove(obj)
		
		if obj in self.delete:
			self.delete.remove(obj)

	def magicSaveAll(self):
		""" Loop through all the list of objects to change and make those changes in persistent storage """

		# insert new objects
		for newObj in self.new:
			M = newObj.mapperClass()
			if M is not None:
				M.insert(newObj)
			else:
				print "Unable to finder mapper for " + str(newObj) + ". Object not being inserted."

		# update changed objects
		for changedObj in self.dirty:
			M = changedObj.mapperClass()
			if M is not None:
				M.update(changedObj)
			else:
				print "Unable to finder mapper for " + str(changedObj) + ". Object not being updated."

		# delete old objects
		for delObj in self.delete:
			if M is not None:
				M = delObj.mapperClass()
				M.delete(delObj)
			else:
				print "Unable to finder mapper for " + str(delObj) + ". Object not being deleted."

		# reset all lists to empty
		self.new = []
		self.dirty = []
		self.delete = []