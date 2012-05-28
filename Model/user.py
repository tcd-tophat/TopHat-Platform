import re

import domainobject
import domainexception
import metadomainobject

class User(metadomainobject.MetaDomainObject):

	__name = "Anonymous"
	__photo = None
	__email = None
	__password = None
	
	def __init__(self, ids=None):
		super(User, self).__init__(ids)

	def __str__(self):
		return str(self.getId()) + " " + self.__name + " " + self.__email + " " + self.__photo

	# setters #
	def setName(self, name):
		name = str(name)

		if len(name) > 60:
			raise domainexception.DomainException("User's name must be less than 60 characters")

		self.__name = name

	def setPhoto(self, photo):
		photo = str(photo)

		if len(photo) is not 32:
			raise domainexception.DomainException("That is not a photo")

		self.__photo = photo

	def setEmail(self, email):
		email = str(email)

		pattern = r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"
		if not re.match(pattern, email):
			raise domainexception.DomainException("That is not a valid email address")

		# email checking needs to be added to user
		self.__email = email

	def setPassword(self, password):
		password = str(password)

		if len(password) is not 64:
			raise domainexception.DomainException("Password variable in the User object must be a 64 character string")

		self.__password = password

	# getters #
	def getName(self):
		return self.__name

	def getPhoto(self):
		return self.__photo

	def getEmail(self):
		return self.__email

	def getPassword(self):
		return self.__password