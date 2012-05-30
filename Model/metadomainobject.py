from abc import ABCMeta, abstractmethod
import domainobject
import domainexception
import metadataobject

class MetaDomainObject(domainobject.DomainObject):
	__metaclass__ = ABCMeta

	_data = {}					# dictionary of meta data objects

	def __init__(self, id_=None):
		self._data = {}

		super(MetaDomainObject, self).__init__(id_)

	def __getattr__(self, attr):
		"""Searches through the object dictionary and the data dictionary to find the variable"""
		if attr in self.__dict__:
			return self.__dict__[attr]

		if attr in self._data:
			return self._data[attr].getValue()			# return that value of the meta data object not the object itself

		raise AttributeError

	def __setattr__(self, attr, value):
		"""Ensures that the data dictionary is not being overwritten then calls DomainObject __setattr__"""
		if attr is "_data": 				# ensure not overriding the data dictionary with some arbitary attribute value
			return None

		if attr in dir(self):
			self.__dict__[attr] = value

		else:
			metaData = metadataobject.MetaDataObject()
			metaData.setKey(attr)
			metaData.setValue(value)
			self._data[attr] = metaData

	def addMetaData(self, metaData):
		"""Adds a meta data object to the dictionary of meta data objects"""
		if not isinstance(metaData, metadataobject.MetaDataObject):
			raise domainexception.DomainException("You must pass in a valid meta data object")

		self._data[metaData.getKey()] = metaData