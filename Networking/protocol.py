from abc import ABCMeta, abstractmethod

class Protocol:

	__metaclass__ = ABCMeta

	@abstractmethod
	def _registerStatusCodes(self):
		pass

