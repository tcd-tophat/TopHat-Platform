from abc import ABCMeta, abstractmethod
from Mapper import objectwatcher
import domainexception

class DomainObject(object):
	"""Abstract base class for any object that is compatible with the Mapper for storage in the persistent storage"""
	__metaclass__ = ABCMeta

	__id = -1				# setup deafult id outside db storage range

	def __init__(self, id=None):
		# check valid id value (pos int)
		if id is not None:
			self.__id = id
		else:
			self.__markNew()			# when the object is created without an id it is marked new / for insertion into persistent storage

		self.__markClean()				# during setup we have updated some of the attributes, make sure we don't update DB without any changes

	def __setattr__(self, attr, value):
		"""Whenever an attribute of this object is changed the object is marked dirty and needs to be updated in persistent storage"""
		if attr in self.__dict__:					# check the attr exists
			prevValue = self.__dict__[attr]			# if so set the prevValue to its value
		else:
			prevValue = None

		self.__dict__[attr] = value					# set the attribute in the dictionary

		if prevValue != value: 						# when any attribute is changed the object is marked for update
			self.__markDirty()							

	def __str__(self):
		return str(self.__class__) + str(self.__id)

	# Getters and Setters #
	def getId(self):
		return self.__id

	def setId(self, value):
		try:
			value = int(value)
		except TypeError:
			raise domainexception.DomainException("The id must be an integer")

		if value < 0:
			raise domainexception.DomainException("The id must be greater than one")

		self.__id = id

	# Object Watcher Functions #
	def __markDirty(self):
		ow = objectwatcher._Objectwatcher()
		ow.addDirty(self)

	def __markNew(self):
		ow = objectwatcher._Objectwatcher()
		ow.addNew(self)

	def __markDelete(self):
		ow = objectwatcher._Objectwatcher()
		ow.addDelete(self)

	def __markClean(self):
		ow = objectwatcher._Objectwatcher()
		ow.addClean(self)

	def markClean(self):
		self.__markClean()

	def mapperClass(self):
		"""Returns the mapper object that this class should use to map this object to storage"""
		mapperName = str(self.__class__.__name__) + "Mapper"
		moduleName = "Mapper." + mapperName.lower()

		try:
			mapperModule = __import__(moduleName, fromlist=["Mapper"])				# import the class
			
			for name in dir(mapperModule):
				try:
					# create a new instance of the mapper class and return it
					M = getattr(mapperModule, mapperName)()							
					return M

				except:
					print "Cannot create Mapper object"
					return None

		except ImportError:
			print "Unable to import Mapper." + moduleName + ". It does not exist"
			return None