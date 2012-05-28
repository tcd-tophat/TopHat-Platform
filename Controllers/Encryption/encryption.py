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
