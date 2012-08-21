from datetime import datetime
from Model.domainobject import DomainObject
from Model.domainexception import DomainException

class Game(DomainObject):

	_name = "Unnamed Game"		# public name of the game 
	_creator = None 			# user who created the game
	_gameType = None			# type of game by id
	_time = None
	_startTime = None
	_endTime = None

	_players = None				# collection of players

	def __init__(self, id_=None):
		super(Game, self).__init__(id_)

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
			raise DomainException("The name of a game cannot be more than 255 characters")

		self._name = name

	def setCreator(self, creator):
		from Model.user import User

		if not isinstance(creator, User):
			raise DomainException("Creator must be an instance of the User object")

		self._creator = creator

	def setGameType(self, gameType):
		from Model.gametype import GameType

		if not isinstance(gameType, GameType):
			raise DomainException("gametype must be an instance of the GameType object")

		self._gameType = gameType

	def setTime(self, time):
		if type(time) is not datetime:
			raise DomainException("Time attribute must be a datetime object not a %s" % str(type(time)))

		self._time = time

	def setStartTime(self, time):
		if type(time) is not datetime and time is not None:
			raise DomainException("The start time must be either empty or a datetime object not %s" % str(type(time)))

		self._startTime = time

	def setEndTime(self, time):
		if type(time) is not datetime and time is not None:
			raise DomainException("The end time must be either empty or a datetime object not %s" % str(type(time)))

		self._endTime = time

	def getPlayers(self):
		# check have we gotten the list already
		if self._players is None:
			from Model.Mapper.playermapper import PlayerMapper
			PM = PlayerMapper()
			self._players = PM.getPlayersInGame(self)

		return self._players

	def dict(self, depth=0):
		if depth < 0:
			return { "id": self.getId() }
		else:
			playerlist = []
			players = self.getPlayers()
			if players:
				for player in players:
					playerlist.append(player.dict(depth-1))

			if self.getStartTime() > datetime.now():
				started = True
			else:
				started = False

			if self.getTime() is not None:
				return {
					"id": self.getId(),
					"name": self.getName(),
					"game_type": self.getGameType().dict(depth-1),
					"time": str(self.getTime()),
					"players": playerlist,
					"creator": self.getCreator().dict(depth-1),
					"start_time": str(self.getStartTime()),
					"end_time": str(self.getEndTime()),
					"started": started
				}
			else:
				return {
					"id": self.getId(),
					"name": self.getName(),
					"game_type": self.getGameType().dict(depth-1),
					"players": playerlist,
					"creator": self.getCreator().dict(depth-1),
					"start_time": str(self.getStartTime()),
					"end_time": str(self.getEndTime()),
					"started": started
				}