from abc import ABCMeta, abstractmethod

class Network:

	__metaclass__ = ABCMeta

	@abstractmethod
	def _registerStatusCodes(self):
		pass

