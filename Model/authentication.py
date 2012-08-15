from Request.requesterrors import Unauthorised, Forbidden

def require_login(func):
	def wrapper(self, *args, **kwargs):
		
		# User has not been loaded
		if self.user is None:
			raise Unauthorised()

		return func(self, *args, **kwargs)
	return wrapper
	
def require_super_user(func):
	def wrapper(self, *args, **kwargs):
		
		# User has not been loaded
		if self.user is None:
			raise Unauthorised()

		elif self.user.accessLevel('super_user'):
			raise Forbidden()

		return func(self, *args, **kwargs)
	return wrapper
	