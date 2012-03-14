class _Objectwatcher:

	objects{} = None					# dictionary of all the objects in the system
	new[] = None						# list of objects to be inserted into the database
	dirty[] = None						# list of objects to be updated
	delete[] = None						# list of objects to be deleted
	
	# make it a singleton class
	def __call__(self):
		return self

	def add(self, obj):
		if isinstance(obj, DomainObject):
			key = self.getGlobalName()
			self.objects[key] = obj
		else:
			raise Exception("Only DomainObjects can be stored in the ObjectWatcher's list")

	def exists(self, classname, id):
		name = classname + "." + id
		if name in objects
			return objects[name]
		else:
			return None

	def getGlobalName(self, obj) :
		""" Gets the global name of this object to be used as the key in the hash map """

		return obj.__class__.__name__ + "." + obj.id


	def addNew(self, obj):
		""" Marks a new object so that it can be inserted into the database """
		new.append(obj)

	def addDelete(self, obj):
		""" Marks an old object that needs to be deleted from the database """
		delete.append(obj)

	def addDirty(self, obj):
		""" Marks an object that has changed and needs to be updated """
		dirty.append(obj)

	def magicSaveAll(self):
		""" Loop through all the list of objects to change and do the changes """

		# insert new objects
		for newObj in self.new:
			print "Inserting: " + newObj
			newObj.mapper().insert(newObj)

		# update changed objects
		for changedObj in self.dirty:
			print "Updating: " + newObj
			changedObj.mapper().update(changedObj)

		# delete old objects
		for delObj in self.delete:
			print "Deleting: " + delObj
			delObj.mapper().delete(delObj)

		# reset all lists to empty
		self.new = []
		self.dirty = []
		self.delete = []

		
