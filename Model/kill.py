from datetime import datetime
from Model.domainobject import DomainObject
from Model.player import Player
from Model.game import Game
from Model.domainexception import DomainException

class Kill(DomainObject):
	
	_killer = None	
	_victim = None
	_verified = False
	_time = None
	_game = None

	def __init__(self, id_=None):
		super(Kill, self).__init__(id_)

		self._time = datetime.now()


	def __str__(self):
		string = self._killer.getName() + " killed " + self._victim.getName() + " the kill is "
		if self._verified is False:
			string += "not "
		string += "verified"

		string += " (" + str(self._time) + ")"

		return string

	# Setters #
	def setGame(self, game):
		if not isinstance(game, Game):
			raise DomainException("Game must be a Game object")

		self._game = game

	def setKiller(self, killer):
		if not isinstance(killer, Player):
			raise DomainException("Killer must be a Player object")

		self._killer = killer

	def setVictim(self, victim):
		if not isinstance(victim, Player):
			raise DomainException("Victim must be a Player object")

		self._victim = victim

	def setVerified(self, value):
		try:
			value = bool(value)				# converts it to boolean type (1 = True and 0 = False)
		except NameError:
			raise DomainException("You can only set verified to true or false")

		self._verified = value

	def setTime(self, time_):
		if type(time_) is "<type 'datetime.datetime'>":
			raise DomainException("Time must a datetime object")

		self._time = time_

	# Getters #
	def getGame(self):
		return self._game

	def getKiller(self):
		return self._killer

	def getVictim(self):
		return self._victim

	def getVerified(self):
		return self._verified

	def getTime(self):
		return self._time

	def dict(self, depth=0):
		if depth < 0:
			return { "id": self.getId() }
		else:
			return {
				"id": self.getId(),
				"verified": self.getVerified(),
				"time": str(self.getTime()),
				"victim": self.getVictim().dict(depth-1),
				"killer": self.getKiller().dict(depth-1),
				"game": self.getGame().dict(depth-1)
			}