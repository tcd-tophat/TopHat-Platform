class User(DomainObject):

	name = None
	photo = None
	email = None
	
	def __init__(self, id):
		super(User, self).__init__(id)

