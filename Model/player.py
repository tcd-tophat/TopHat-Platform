import domainOobject
import user
import game
import domainexception

class Player(domainobject.DomainObject):

	__name = "Anonymous" 
	__photo = None 
	__game = None	
	__user = None
	__lat = 0.0			
	__lon = 0.0 			
	__score = 0			
	__time = 0 		

	def __init__(self, id_=None):
		super(Player, self).__init__(id_)

	def __str__(self):
		return self.__name + " in game " + self.__game.__name + " is user " self.__user.__name + " has a score of " + self.__time

	# Setters #
	def setName(self, name):
		if len(name) > 60:
			raise domainexception.DomainException("Name of player must be less than 60 characters")

		self.__name = name

	def setPhoto(self, photo):
		if len(photo) not 32:
			raise domainexception.DomainException("Photo must be a 32 character string")

		self.__photo = photo

	def setGame(self, game):
		if is not isinstance(game, game.Game):
			raise domainexception.DomainException("Game attribute must be a reference to another Game object")

		self.__game = game

	def setUser(self, user):
		if is not isinstance(user, user.User):
			raise domainexception.DomainException("User attribute must be a reference to another User object")

	def setLat(self, lat):
		# type checking required
		self.__lat = lat

	def setLon(self, lon):
		# type checking required
		self.__lon = lon

	def setScore(self, score):
		try:
			score = int(score)
		except ValueError:
			raise domainexception.DomainException("Score must be an integer")

		if score > 99999 or score < -99999:
			raise domainexception.DomainException("Score must be between -99999 and +99999")

		self.__score = score

	def setTime(self, time):
		try:
			time = int(time)
		except ValueError:
			raise domainexception.DomainExceptionm("Time must be an int - of seconds since Jan 1st 1972 UTC")

	# Getters #
	def getName(self):
		return self.__name	

	def getPhoto(self):
		return self.__photo

	def getGame(self):
		return self.__game

	def getUser(self):
		return self.__user	

	def getLat(self):
		return self.__lat

	def getLon(self):
		return self.__lon

	def getScore(self):
		return self.__score

	def getTime(self):
		return self.__time