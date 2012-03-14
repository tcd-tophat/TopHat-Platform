from abc import ABCMeta, abstractmethod
from Mapper import _ObjectWatcher

class DomainObject:
	__metaclass__ = ABCMeta

	id = -1				# setup deafult id outside db storage range

	def __init__(self, id = None):
		# check valid id value (pos int)
		if id is not None:
			self.id = id
		else:
			self.markNew()			# when the object is created without an id it is marked for insertion

	def __setattr__(self, attr, value):
		self.markDirty()			# when any attribute is changed the object is marked for update

	def __str__(self):
		str = __class__.__name__ + " " + id + "\n"
		str += vars(self)

	def __markDitry(self):
		_ObjectWatcher.addDirty(self)

	def __markNew(self):
		_ObjectWatcher.addNew(self)

	def __markDelete(self):
		_ObjectWatcher.addDelete(self)

	def mapper(self):
		return __class__.__name__ + "Mapper"

	def collection(self):
		return __class__.__name__ + "Collection"