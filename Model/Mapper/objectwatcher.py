class _Objectwatcher:

	objects{} = None					# dictionary of all the objects in the system
	
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
		
