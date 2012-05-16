import DomainObject

class User(DomainObject.DomainObject):

	name = "Anonymous"				# 60 characterss
	photo = None			# 32 chars
	email = None			# 255 chars
	
	def __init__(self, id = None):
		super(User, self).__init__(id)

	def __str__(self):
		return str(self.id) + " " + self.name + " " + self.email + " " + self.photo