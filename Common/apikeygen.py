from os import urandom

def getKey():
	return urandom(64).encode('hex')[:64]