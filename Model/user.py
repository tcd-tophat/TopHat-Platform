import re
from datetime import datetime
import domainobject
import domainexception
import metadomainobject

class User(metadomainobject.MetaDomainObject):

	_name = "Anonymous"
	_photo = None
	_email = None
	_password = None
	_time = None
	
	def __init__(self, id_=None):
		super(User, self).__init__(id_)

	def __str__(self):
		return str(self.getId()) + " " + self._name + " " + str(self._email) + " " + str(self._photo)

	# setters #
	def setName(self, name):
		if len(name) > 60:
			raise domainexception.DomainException("User's name must be less than 60 characters")

		self._name = name

	def setPhoto(self, photo):
		if len(photo) is not 32:
			raise domainexception.DomainException("That is not a photo")

		self._photo = photo

	def setEmail(self, email):
		email = str(email)

		pattern = r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"
		if not re.match(pattern, email):
			raise domainexception.DomainException("That is not a valid email address")

		# email checking needs to be added to user
		self._email = email

	def setPassword(self, password):
		password = str(password)

		self._password = password

	def setTime(self, time):
		if type(time) is not datetime:
			raise domainexception.DomainException("Time must be a datetime object, not a %s" % type(time))

		self._time = time

	# getters #
	def getName(self):
		return self._name

	def getPhoto(self):
		return self._photo

	def getEmail(self):
		return self._email

	def getPassword(self):
		return self._password

	def getTime(self):
		return self._time