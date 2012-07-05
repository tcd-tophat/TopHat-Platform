
def requirelogin(func):
	print "I don't have a clue about login, but go on!"
	return func

def requireapitoken(func):
	print "Require API Token"
	return func