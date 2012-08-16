from datetime import datetime
import domainobject
import user
import gametype
import domainexception
from Model.Mapper.playermapper import PlayerMapper

class Game(domainobject.DomainObject):

	_name = "Unnamed Game"		# public name of the game 
	_creator = None 			# user who created the game
	_gameType = None			# type of game by id
	_time = None
	_startTime = None
	_endTime = None

	_players = []				# collection of players

	def __init__(self, id_=None):
		super(Game, self).__init__(id_)

		self._players = []

	def __str__(self):
		return str(self.getId()) + " Name " + ": " + self._name + "  created by {" + str(self._creator) + "}  - GameType: "+str(self._gameType.getId())

	def getName(self):
		return self._name

	def getCreator(self):
		return self._creator

	def getGameType(self):
		return self._gameType

	def getTime(self):
		return self._time

	def getStartTime(self):
		return self._startTime

	def getEndTime(self):
		return self._endTime

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
			raise domainexception.DomainException("Time attribute must be a datetime object not a %s" % str(type(time)))

		self._time = time

	def setStartTime(self, time):
		if type(time) is not datetime and time is not None:
			raise domainexception.DomainException("The start time must be either empty or a datetime object not %s" % str(type(time)))

		self._startTime = time

	def setEndTime(self, time):
		if type(time) is not datetime and time is not None:
			raise domainexception.DomainException("The end time must be either empty or a datetime object not %s" % str(type(time)))

		self._endTime = time

	def getPlayers(self):
		# check have we gotten the list already
		if self._players:
			PM = PlayerMapper()
			self._players = PM.getPlayersInGame(self)

		return self._players

	def dict(self, depth=0):
		if depth < 0:
			return { "id": self.getId() }
		else:
			playerlist = []
			if self.getPlayers() is not None:
				if depth > 0: # only get if not excessive
					for player in self.getPlayers():
						playerlist.append(player.dict(depth-1))

			if self.getTime() is not None:
				return {
					"id": self.getId(),
					"name": self.getName(),
					"game_type": self.getGameType().dict(depth-1),
					"time": str(self.getTime()),
					"players": playerlist,
					"creator": self.getCreator().dict(depth-1)
				}
			else:
				return {
					"id": self.getId(),
					"name": self.getName(),
					"game_type": self.getGameType().dict(depth-1),
					"players": playerlist,
					"creator": self.getCreator().dict(depth-1)
				}