from Request.requesterrors import Unauthorised

def require_login(func):
	def wrapper(self, *args, **kwargs):
		
		# User has not been loaded
		if self.user is None:
			raise Unauthorised("You must be authenticated in order to use this resource.")

		return func(self, *args, **kwargs)
	return wrapper
	
def require_super_user(func):
	def wrapper(self, *args, **kwargs):
		
		# User has not been loaded
		if self.user is None:
			raise Unauthorised("You must be authenticated in order to use this resource.")

		elif self.user.accessLevel('super_user'):
			raise Unauthorised("You must be authenticated with sufficient priviliges in order to use this resource.")

		return func(self, *args, **kwargs)
	return wrapper
	