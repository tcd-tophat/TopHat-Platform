from abc import ABCMeta, abstractmethod
import domainobject
import domainexception

class MetaDomainObject(domainobject.DomainObject):
	__metaclass__ = ABCMeta

	__data[]					# dictionary of meta data objects

	def __init__(self, id=None):
		super(MetaDomainObject, self).__init__(id)

	def __getattr__(self, attr):
		""" Searches through the object dictionary and the data dictionary to find the variable """

		# check the list of local variables
		if attr in self.__dict__:
			return self.__dict__[attr]

		if attr in self.__data:
			return self.__data[attr].value				# return that value of the meta data object not the object itself

		return None

	def __setattr__(self, attr, value):
		""" Ensures that the data dictionary is not being overwritten then calls DomainObject __setattr__ """
		if attr == "data": 				# ensure not overriding the data dictionary with some arbitary attribute value
			raise domainexception.DomainException("You cannot alter the data attribute of a MetaDomainObject " + self.__class___._name__ + " (" + self.id + ")")

		# call the parent implementation to handle the rest
		super(MetaDomainObject, self).__setattr__(attr, value)