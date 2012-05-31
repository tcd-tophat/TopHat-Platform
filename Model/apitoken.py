import domainobject

class Apitoken(domainobject.Domainobject):

	_token = None

	def __init__(self, id_=None):
		super(Apitoken, self).__init__(id_)

	def setToken(self, token):
		self._token = token

	def getToken(self):
		return self._token