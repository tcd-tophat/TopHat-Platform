from socket import socket
from abc import abstractmethod, ABCMeta

class Encryption:

		__metaclass__=ABCMeta
		
		@abstractmethod
		def __init__(self,_sock):
				self._sock=_sock
		
		@abstractmethod
		def send(self):
				pass
		@abstractmethod
		def recv(self):
				pass

		@abstractmethod
		def setblocking(self):
				pass

		@abstractmethod
		def fileno(self):
				pass
		
		@abstractmethod
		def getpeername(self):
				pass
		
		@abstractmethod
		def close(self):
				pass

		@abstractmethod
		def getsockopt(self, *arg):
				pass

		@abstractmethod
		def configKeys(slef):
				pass
