from abc import ABCMeta, abstractmethod
import domainobject
import domainexception

class MetaDataObject(domainobject.DomainObject):
	""" 
		Abstract container that extends DomainObject for meta data records for Domain Model objects. 
		Objects are used instead of straight variables so that it intergrates with Mapper better.
	"""
	__metaclass__ = ABCMeta

	_key = ""				# 30 char
	_value = ""			# text

	def __init__(self, id_=None):
		super(MetaDataObject, self).__init__(id_)

	def setKey(self, value):
		# Check length
		if len(value) > 30:
			raise domainexception.DomainException("Key must be less than 30 characters long")

		self._key = value

	def getKey(self):
		return self._key

	def setValue(self, value):
		self._value = value

	def getValue(self):
		return self._value