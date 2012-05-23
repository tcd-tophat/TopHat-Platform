from abc import ABCMeta, abstractmethod
import domainobject
import domainexception
import metadataobject

class MetaDomainObject(domainobject.DomainObject):
	__metaclass__ = ABCMeta

	__data = {}					# dictionary of meta data objects

	def __init__(self, id_=None):
		super(MetaDomainObject, self).__init__(id_)

	def __getattr__(self, attr):
		"""Searches through the object dictionary and the data dictionary to find the variable"""

		# check the list of local variables
		if attr in self.__dict__:
			return self.__dict__[attr]

		if attr in self.__data:
			return self.__data[attr].getValue()				# return that value of the meta data object not the object itself

		return None

	def __setattr__(self, attr, value):
		"""Ensures that the data dictionary is not being overwritten then calls DomainObject __setattr__"""
		if attr == "data": 				# ensure not overriding the data dictionary with some arbitary attribute value
			raise domainexception.DomainException("""You cannot alter the data attribute of a MetaDomainObject """
													+ self.__class___._name__ + " (" + self.id + ")")

		try:
			self.__data[attr].setValue(value) 	# attr already in meta data dictionary - update it

		except KeyError:
			# there is no attr of this name in the dictionary create a meta data  in the meta data dictionary
			metaData = metadataobject.MetaDataObject()
			metaData.setKey(attr)
			metaData.setValue(attr)
			self.__data[attr] = metaData

		# call the parent implementation to handle the rest
		super(MetaDomainObject, self).__setattr__(attr, value)

	def addMetaData(self, metaData):
		"""Adds a meta data object to the dictionary of meta data objects"""
		self.__data[metaData.getKey()] = metaData