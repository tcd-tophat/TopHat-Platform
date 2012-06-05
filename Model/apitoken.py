import domainobject
import domainexception

class Apitoken(domainobject.DomainObject):

	_token = None

	def __init__(self, id_=None):
		super(Apitoken, self).__init__(id_)

	def __str__(self):
		return "APIToken: " + self._token

	def setToken(self, token):
		if len(token) != 64:
			raise domainexception.DomainException("That is not a valid API Token, should be a 64 character hash")

		self._token = token

	def getToken(self):
		return self._token