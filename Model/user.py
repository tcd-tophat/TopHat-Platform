import re

import domainobject
import domainexception

class User(domainobject.DomainObject):

	__name = "Anonymous"
	__photo = None
	__email = None
	
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

		
		#if not re.match(r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+(?:[A-Z]{2}|com|org|net|edu|gov|mil|biz|info|mobi|name|aero|asia|jobs|museum)\b", email):
		if not re.match(r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?", email):
			raise domainexception.DomainException("That is not a valid email address")

		# email checking needs to be added to user
		self.__email = email

	# getters #
	def getName(self):
		return self.__name

	def getPhoto(self):
		return self.__photo

	def getEmail(self):
		return self.__email