import random

class ApiKeyGen(object):

	@staticmethod
	def getKey():

		hash_ = random.getrandbits(256)

		return hex(hash_)[2:-1]