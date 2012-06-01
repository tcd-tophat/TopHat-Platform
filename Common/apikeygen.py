import random
	def getKey():
		return hex(random.getrandbits(256))[2:-1]