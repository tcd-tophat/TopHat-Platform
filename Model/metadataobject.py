from abc import ABCMeta, abstractmethod
import domainobject
import domainexception

class MetaDataObject(domainobject.DomainObject):
	""" 
		Abstract meta data container that extends DomainObject for meta data records for Domain Model objects. 
		Objects are used instead of straight variables so that it intergrates with Mapper better.
	"""
	__metaclass__ = ABCMeta

	_key = ""				# 30 char
	_value = ""				# text
	_object = ""			# reference to the object that this meta data object is for

	def __init__(self, id_=None):
		super(MetaDataObject, self).__init__(id_)

	def __str__(self):
		return str(self.getId()) + " " + str(self._key) + " : " + str(self._value)

	def setKey(self, value):
		# Check length
		if len(value) > 30:
			raise domainexception.DomainException("Key must be less than 30 characters long")

		self._key = value

	def getKey(self):
		return self._key

	def setValue(self, value):
		self._value = str(value)

	def getValue(self):
		return self._value

	def setObject(self, obj):
		if not isinstance(obj, domainobject.DomainObject):
			raise domainexception.DomainException("A MetaDataObject's reference object must be another domainobject")

		self._doSetObject(obj)

		# add reference in the Reference object to this meta data object
		obj.addMetaData(self)

	@abstractmethod
	def _doSetObject(self, obj):
		pass

	@abstractmethod
	def getObject(self):
		pass