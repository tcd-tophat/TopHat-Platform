from Request.requesterrors import Unauthorised

def requirelogin(func):
	def wrapper(self, *args, **kwargs):
		
		# User has not been loaded
		if self.user == None:
			raise Unauthorised("You must be authenticated in order to use this resource.")
		return func(self, *args, **kwargs)
	return wrapper
	