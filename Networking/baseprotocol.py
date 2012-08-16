from abc import ABCMeta, abstractmethod

class BaseProtocol:

	__metaclass__ = ABCMeta

	_config = None

	def __init__(self, config):
		self._config = config

