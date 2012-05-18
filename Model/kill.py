import domainobject
import user
import domainexception

class Kill(domainobject.DomainObject):
	
	__killer = None	
	__victim = None
	__verified = False
	__time = 0

	def __init__(self, id_=None):
		super(Kill, self).__init__(id_)

	def __str__(self):
		string = self.__killer.__name + " killed " + self.__victim.__name + " the kill is "
		if self.__verified is False:
			string += " not "
		string += "verified"

		return string

	# Setters #
	def setKiller(self, value):
		if type(killer) is not user.User:
			raise domainexception.DomainException("Killer must be a User object")

		self.__killer = value

	def setVictim(self, victim):
		if type(victim) is not user.User:
			raise domainexception.DomainException("Victim must be a User Object")

		self.__victim = victim

	def setVerified(self, value):
		try:
			value = bool(value)				# converts it to boolean type (1 = True and 0 = False)
		except NameError:
			raise domainexception.DomainException("You can only set verified to true or false")

		self.__verified = value

	def setTime(self, time):
		try:
			time = int(time)
		except ValueError:
			raise domainexception.DomainException("Time must be UTC in seconds from 1972")

		self.__time = time

	# Getters #
	def getKiller(self):
		return self.__killer

	def getVictim(self):
		return self.__victim

	def getVerified(self):
		return self.__verified

	def getTime(self):
		return self.__time