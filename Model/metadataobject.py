from abc import ABCMeta, abstractmethod
import domainobject
import domainexception

class MetaDataObject(domainobject.DomainObject):
	""" Abstract container that extends DomainObject for meta data records for Domain Model objects. Objects are used instead of straight variables so that it intergrates with Mapper better """"
	__metaclass__ = ABCMeta

	__key = None				# 30 char
	__value = None			# text

	def _init__(self, id=None, key=None, value=None):
		super(MetaDataObject, self)._init(id)

	def setKey(self, value):
		# Check length
		if len(value) > 30:
			raise domainexception.DomainException("Key must be less than 30 characters long")

		self.__key = value

	def getKey(self):
		return self.__key

	def setValue(self, value):
		self.__value = value

	def getValue(self):
		return self.__value