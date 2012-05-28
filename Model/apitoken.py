import domainobject

class Apitoken(domainobject.Domainobject):

	__token = None

	def __init__(self, id_=None):
		super(Apitoken, self).__init__(id_)

	def setToken(self, token):
		self.__token = token

	def getToken(self):
		return self.__token