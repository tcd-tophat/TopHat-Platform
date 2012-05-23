from abc import ABCMeta, abstractmethod
import domainobject
import domainexception

class MetaDataObject(domainobject.DomainObject):
	""" 
		Abstract container that extends DomainObject for meta data records for Domain Model objects. 
		Objects are used instead of straight variables so that it intergrates with Mapper better.
	"""
	__metaclass__ = ABCMeta

	__key = ""				# 30 char
	__value = ""			# text

	def __init__(self, id_=None, key=None, value=None):
		super(MetaDataObject, self).__init__(id_)

		self.__key = key
		self.__value = value

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