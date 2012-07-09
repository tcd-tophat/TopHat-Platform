import domainobject
import domainexception
import user

class Apitoken(domainobject.DomainObject):

	_token = None
	_user = None

	def __init__(self, id_=None):
		super(Apitoken, self).__init__(id_)

	def __str__(self):
		str_ = "APIToken: " + self._token

		if self._user is not None:
			str_ += " (User: " + str(self._user) + ")"

		return str_

	def setToken(self, token):
		if len(token) != 64:
			raise domainexception.DomainException("That is not a valid API Token, should be a 64 character hash")

		self._token = token

	def getToken(self):
		return self._token

	def setUser(self, user_):
		if not isinstance(user_, user.User):
			raise domainexception.DomainException("Must reference a User object not a %s" % str(type(user_)))

		self._user = user_

	def getUser(self):
		return self._user

	def dict(self):
		return {
			"user": self.getUser().dict(),
			"apitoken": self.getToken()
		}