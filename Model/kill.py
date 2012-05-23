import domainobject
import player
import domainexception

class Kill(domainobject.DomainObject):
	
	__killer = None	
	__victim = None
	__verified = False
	__time = 0

	def __init__(self, id_=None):
		super(Kill, self).__init__(id_)

	def __str__(self):
		string = self.__killer.getName() + " killed " + self.__victim.getName() + " the kill is "
		if self.__verified is False:
			string += " not "
		string += "verified"

		string += " (" + str(self.__time) + ")"

		return string

	# Setters #
	def setKiller(self, killer):
		if not isinstance(killer, player.Player):
			raise domainexception.DomainException("Killer must be a Player object")

		self.__killer = killer

	def setVictim(self, victim):
		if not isinstance(victim, player.Player):
			raise domainexception.DomainException("Victim must be a Player Object")

		self.__victim = victim

	def setVerified(self, value):
		try:
			value = bool(value)				# converts it to boolean type (1 = True and 0 = False)
		except NameError:
			raise domainexception.DomainException("You can only set verified to true or false")

		self.__verified = value

	def setTime(self, time_):
		if type(time_) is "<type 'datetime.datetime'>":
			raise domainexception.DomainException("Time must a datetime object")

		self.__time = time_

	# Getters #
	def getKiller(self):
		return self.__killer

	def getVictim(self):
		return self.__victim

	def getVerified(self):
		return self.__verified

	def getTime(self):
		return self.__time