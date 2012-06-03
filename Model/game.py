from datetime import datetime
import domainobject
import user
import domainexception

class Game(domainobject.DomainObject):

	_name = "Unnamed Game"		# public name of the game 
	_creator = None 			# user who created the game
	_gameTypeId = None			# type of game by id
	_gameTypeName = ""			# public name of game type
	_time = None

	def __init__(self, id_=None):
		super(Game, self).__init__(id_)

	def __str__(self):
		return str(self.getId()) + " " + self._gameTypeName + ": " + self._name + "  created by " + self._creator.getName() + " (" + str(self._creator.getId()) + ")"

	def getName(self):
		return self._name

	def getCreator(self):
		return self._creator

	def getGameTypeId(self):
		return self._gameTypeId	

	def getGameTypeName(self):
		return self._gameTypeName

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

	def setGameTypeId(self, id_):
		id_ = int(id_)
		
		if id_ > 99999 or id_ < 0:
			raise domainexception.DomainException("Game Type id must be a positive int less than 99999")

		self._gameTypeId = id_

	def setGameTypeName(self, name):
		if len(name) > 50:
			raise domainexception.DomainException("Name of the Game type must be less that 50")

		self._gameTypeName = name

	def setTime(self, time):
		if type(time) is not datetime:
			raise domainexception.DomainException("Time attribute must be a datetime object not a %s" % type(time))

		self._time = time