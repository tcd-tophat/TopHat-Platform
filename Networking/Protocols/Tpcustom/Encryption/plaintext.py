
from encryption import Encryption
class Plaintext(Encryption):

		def __init__(self, _sock, **kwargs):
				super(Plaintext, self).__init__(_sock)


		def recv(self, size):
				return self._sock.recv(size)

		def send(self,data):
				return self._sock.send(data)
		
		def fileno(self):
				return self._sock.fileno()
		
		def setblocking(self, flag):
				return self._sock.setblocking(flag)
		
		def getpeername(self):
				return self._sock.getpeername()

		def close(self):
				return self._sock.close()
		
		def getsockopt(self, *args):
				return self.sock.getsockopt(self, *args)
		def initialized(self):
				return True

		@staticmethod
		def configKeys():
				return []
