import re
import Model
from datetime import datetime
from Model import domainobject
from Model import domainexception
from Model import metadomainobject
from Model.game import Game
from Model.apitoken import Apitoken
from Common.passHash import makeHash

class User(metadomainobject.MetaDomainObject):

	_name = "Anonymous"
	_photo = None
	_email = None
	_password = None
	_token = None
	_time = datetime.now()

	# collection vars
	_games = None

	# magic methods
	def __init__(self, id_=None):
		super(User, self).__init__(id_)

		#For some reason we are having errors due to the games variable.
		self._games = None

	def __str__(self):
		return str(self.getId()) + " " + self._name + " " + str(self._email)

	# setters #
	def setName(self, name):
		if len(name) > 60:
			raise domainexception.DomainException("User's name must be less than 60 characters")

		self._name = name

	def setPhoto(self, photo):
		if photo is not None:
			if len(photo) is not 32:
				raise domainexception.DomainException("That is not a photo")

		self._photo = photo

	def setEmail(self, email):
		email = str(email)

		pattern = r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"
		if not re.match(pattern, email):
			raise domainexception.DomainException("That is not a valid email address")

		# email checking needs to be added to user
		self._email = email

	def setPassword(self, password):
		if password is not None:
			password = str(password)

		self._password = password
		

	def setPreHash(self, password):
		self.setPassword(makeHash(password))

	def setTime(self, time):
		if type(time) is not datetime:
			raise domainexception.DomainException("Time must be a datetime object, not a %s" % type(time))

		self._time = time

	def setToken(self, token):
		if token is not None:
			if not isinstance(token, Model.apitoken.Apitoken):
				raise domainexception.DomainException("Token must be an API Token Model Object")

		self._token = token

	def setAccessLevel(self, level):
		if self._token is not None:
			self._token.setGroup(level)
		else:
			raise domainexception.DomainException("Token associated to user is invalid.")

	def accessLevel(self, permission):
		return self._token.checkPermission(permission)

	# getters #
	def getName(self):
		return self._name

	def getPhoto(self):
		return self._photo

	def getEmail(self):
		return self._email

	def getPassword(self):
		return self._password

	def getTime(self):
		return self._time

	def getToken(self):
		return self._token

	def _loadGames(self):
		from Model.Mapper.gamemapper import GameMapper
		GM = GameMapper()
		self._games = GM.findByUser(self)

	def getGames(self):
		if self._games is None:
			self._loadGames()
		return self._games

	def addGame(self, game_):
		if not isinstance(game_, Model.game.Game):
			raise domainexception.DomainException("Must be an instance of the Game Model object")

		self._games.add(game_)

	def dict(self, depth=0):
		if depth < 0:
			return { "id": self.getId() }
		else:
			# build a list of the games' dict
			gameslist = []
			games = self.getGames()
			if games is not None:
				if depth > 0: # only get if not excessive
					for game in self.getGames():
						gameslist.append(game.dict(depth-1))

			return {
				"id": self.getId(),
				"name": self.getName(),
				"email": self.getEmail(),
				"created": str(self.getTime()),
				"photo": str(self.getPhoto()),
				"joined_games": gameslist
			}