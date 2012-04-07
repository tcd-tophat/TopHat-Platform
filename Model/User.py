import DomainObject

class User(DomainObject.DomainObject):

	name = None
	photo = None
	email = None
	
	def __init__(self, id = None):
		super(User, self).__init__(id)