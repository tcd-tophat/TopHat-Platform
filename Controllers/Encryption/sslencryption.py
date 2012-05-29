from encryption import Encryption
from ssl import wrap_socket, SSLSocket, SSLError
from socket import error as SocketError
class SSLEncryption(Encryption):
		def __init__(self, _sock, **kwargs):
				super(SSLEncryption, self).__init__(_sock)
				try:
						self._keyfile = kwargs['keyfile']
						self._certfile= kwargs['certfile']
				except KeyError:
						try:
								self.config = kwargs['config']
								self._keyfile = self.config.SSLKeyPath
								self._certfile = self.config.SSLCertPath
						except KeyError:
								raise TypeError('Expected keyfile, certfile and ca_certs got %s instead.' % str(kwargs))
				self._securesock= wrap_socket(self,keyfile=self._keyfile, server_side=True, certfile=self._certfile, do_handshake_on_connect=True)
		def recv(self, size):
				return self._securesock.read(size)
		def send(self, data):
				return self._securesock.write(data)
		def do_handshake(self):
				return self._securesock.do_handshake()
		def setblocking(self, flag):
				self._securesock.setblocking(flag)
		def fileno(self):
				return self._securesock.fileno()
		def getpeername(self):
				return self._securesock.getpeername()
		def close(self):
				try:
						self._securesock=self._securesock.unwrap()
				except SSLError:
						pass
				except SocketError:
						pass
				except AttributeError:
						pass
				except ValueError:
						pass
				#return self._sock.close()
		def getsockopt(self, *args):
				return self._sock.getsockopt(*args)
		@staticmethod
		def configKeys():
				return ['SSLKeyPath', 'SSLCertPath'] 
