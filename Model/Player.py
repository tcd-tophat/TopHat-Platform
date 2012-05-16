import DomainObject

class Player(DomainObject.DomainObject):

	name = "Anonymous" 			# char 60
	photo = None 			# char 32
	game = None				# Game object
	user = None 			# User Object
	lat = 0.0				# latitude
	lon = 0.0 				# longitude
	score = 0				# players score
	time = 0 				# time of last update to player

	def __init__(self, id = None):
		super(Player, self).__init__(id)

	def __str__(self):
		return self.name + " in game " + self.game.name + " is user " self.user.name + " has a score of " + self.time