from datetime import datetime
import domainobject
import user
import domainexception

class GameType(domainobject.DomainObject):

	_name = "Unnamed Game Type"		# public name of the game type

	def __init__(self, id_=None):
		super(GameType, self).__init__(id_)

	def __str__(self):
		return str(self.getId()) + " " +self._name

	def getName(self):
		return self._name

	def setName(self, name):
		if len(name) > 255:
			raise domainexception.DomainException("The name of a game cannot be more than 255 characters")

		self._name = name

	def dict(self, depth=0):
		if depth < 0:
			return self.getId()
		else:
			return {
				"id": self.getId(),
				"name": self.getName()
			}