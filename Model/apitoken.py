from Model.domainobject import DomainObject
from Model.domainexception import DomainException
from Common import permissions

class Apitoken(DomainObject):

	_token = None
	_user = None
	_group = 1

	def __init__(self, id_=None):
		super(Apitoken, self).__init__(id_)

	def __str__(self):
		str_ = "APIToken: " + self._token

		if self._user is not None:
			str_ += " (User: " + str(self._user) + ")"

		return str_

	def setToken(self, token):
		if len(token) != 64:
			raise DomainException("That is not a valid API Token, should be a 64 character hash")

		self._token = token

	def getToken(self):
		return self._token

	def setUser(self, user_):
		from Model.user import User
		
		if not isinstance(user_, User):
			raise DomainException("Must reference a User object not a %s" % str(type(user_)))

		user_.setToken(self)
		self._user = user_

	def getUser(self):
		return self._user

	def setGroup(self, group):
		self._group = int(group)

	def getGroup(self):
		return self._group

	def dict(self, depth=0):
		if depth < 0 or self.getUser() is None:
			return { "apitoken": self.getToken() }
		else:	
			return {
				"user": self.getUser().dict(depth-1),
				"apitoken": self.getToken()
			}

	def checkPermission(self, permission):
		# check the list of permissions
		if permissions.PERMISSIONS[permission] is self._group:
			return True
		else:
			return False