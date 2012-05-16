import DomainObject

class Game(DomainObject.DomainObject):

	name = None				# public name of the game     (255 characters)
	creator = None 			# user who created the game   (User Object)
	gameTypeId = None		# type of game by id
	gameTypeName = None		# public name of game type    (50 chars)

	def __init__(self, id = None):
		super(Game, self).__init__(id)

	def __str__(self):
		return str(self.id) + " " + self.gameTypeName + ": " + self.name + "  created by " + self.creator.name + " (" + self.creator.id + ")"