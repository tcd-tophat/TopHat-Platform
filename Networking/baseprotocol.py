from abc import ABCMeta, abstractmethod

class BaseProtocol:

	__metaclass__ = ABCMeta

	_config = None

	def __init__(self, config):
		self._config = config

	@abstractmethod
	def loop(self):
		pass

	@abstractmethod
	def bind(self):
		pass

	@abstractmethod
	def _registerStatusCodes(self):
		pass