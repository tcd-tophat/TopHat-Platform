from datetime import datetime
import domainobject
import user
import gametype
import domainexception

class Game(domainobject.DomainObject):

	_name = "Unnamed Game"		# public name of the game 
	_creator = None 			# user who created the game
	_gameType = None			# type of game by id
	_time = None

	def __init__(self, id_=None):
		super(Game, self).__init__(id_)

	def __str__(self):
		return str(self.getId()) + " Name " + ": " + self._name + "  created by " + self._creator.getName() + " (" + str(self._creator.getId()) + ") - GameType: "+self._gameType.getId()

	def getName(self):
		return self._name

	def getCreator(self):
		return self._creator

	def getGameType(self):
		return self._gameType

	def getTime(self):
		return self._time

	def setName(self, name):
		if len(name) > 255:
			raise domainexception.DomainException("The name of a game cannot be more than 255 characters")

		self._name = name

	def setCreator(self, creator):
		if not isinstance(creator, user.User):
			raise domainexception.DomainException("Creator must be an instance of the User object")

		self._creator = creator

	def setGameType(self, gameType):
		if not isinstance(gameType, gametype.GameType):
			raise domainexception.DomainException("gametype must be an instance of the GameType object")

		self._gameType = gameType

	def setTime(self, time):
		if type(time) is not datetime:
			raise domainexception.DomainException("Time attribute must be a datetime object not a %s" % type(time))

		self._time = time

	def dict(self, depth=0):
		if depth < 0:
			return { "id": self.getId() }
		else:
			if self.getTime() is not None:
				return {
					"id": self.getId(),
					"name": self.getName(),
					"game_type": self.getGameType().dict(depth-1),
					"time": str(self.getTime()),
					"creator": self.getCreator().dict(depth-1)
				}
			else:
				return {
					"id": self.getId(),
					"name": self.getName(),
					"game_type": self.getGameType().dict(depth-1),
					"creator": self.getCreator().dict(depth-1)
				}