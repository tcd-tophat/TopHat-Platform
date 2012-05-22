import domainobject
import user
import domainexception

class Game(domainobject.DomainObject):

	__name = "Unnamed Game"				# public name of the game     (255 characters)
	__creator = None 			# user who created the game   (User Object)
	__gameTypeId = None			# type of game by id  		  (smallint(5) unsigned)
	__gameTypeName = ""		# public name of game type    (50 chars)

	def __init__(self, id_=None):
		super(Game, self).__init__(id_)

	def __str__(self):
		return str(self.__id) + " " + self.__gameTypeName + ": " + self.__name + "  created by " 
				+ self.__creator.__name + " (" + self.__creator.__id + ")"

	def getName(self):
		return self.__name

	def getCreator(self):
		return self.__creator

	def getGameTypeId(self):
		return self.__gameTypeId	

	def getGameTypeName(self):
		return self.__gameTypeName

	def setName(self, name):
		if len(name) > 255:
			raise domainexception.DomainException("The name of a game cannot be more than 255 characters")

		self.__name = name

	def setCreator(self, creator):
		if is not isinstance(creator, user.User):
			raise domainexception.DomainException("Creator must be an instance of the User object")

	def setGameTypeId(self, id_):
		if id_ > 99999 or id_ < 0:
			raise domainexception.DomainException("Game Type id must be a positive int less than 99999")

		self.__gameTypeId = id_

	def setGameTypeName(self, name):
		if len(name) > 50:
			raise domainexception.DomainException("Name of the Game type must be less that 50")

		self.__gameTypeName = name
