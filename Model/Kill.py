import DomainObject

class Kill(DomainObject.DomainObject):
	
	killer = None			# User Object
	victim	= None			# User Object
	verified = False		# boolean
	time = 0				# time the kill took place

	def __init__(self, id = None):
		super(Kill, self).__init__(id)

	def __str__(self):
		string = self.killer.name + " killed " + self.victim.name + " the kill is "
		if self.verified is False:
			string += " not "
		string += "verified"

		return string