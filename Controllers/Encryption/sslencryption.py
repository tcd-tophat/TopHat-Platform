from encryption import Encryption
from ssl import wrap_socket, SSLSocket, SSLError, CERT_REQUIRED
from socket import error as SocketError
class SSLEncryption(Encryption):
		def __init__(self, _sock, **kwargs):
				super(SSLEncryption, self).__init__(_sock)
				try:
						self._keyfile = kwargs['keyfile']
						self._certfile= kwargs['certfile']
						self._ca_certs= kwargs['ca_certs']
				except KeyError:
						try:
								self.config = kwargs['config']
								self._keyfile = self.config.SSLKeyPath
								self._certfile = self.config.SSLCertPath
								self._ca_certs = self.config.SSLCAPath
						except KeyError:
								raise TypeError('Expected keyfile, certfile and ca_certs got %s instead.' % str(kwargs))
						
						try:
								self._securesock= wrap_socket(  self,
														keyfile=self._keyfile, 
														ca_certs=self._ca_certs,
														certfile=self._certfile, 
														server_side=True,
#														cert_reqs=CERT_REQUIRED,
														do_handshake_on_connect=True,
											)
						except SSLError:
								print "probs CA loL"
								self._securesock=None
		def recv(self, size):
				return self._securesock.read(size)
		
		def send(self, data):
				return self._securesock.write(data)
		
		def do_handshake(self):
				return self._securesock.do_handshake()
		
		def setblocking(self, flag):
				self._sock.setblocking(flag)
		
		def fileno(self):
				return self._securesock.fileno()
		
		def getpeername(self):
				return self._securesock.getpeername()
		
		def initialized(self):
				return self._securesock is not None
		
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
				return ['SSLKeyPath', 'SSLCertPath', 'SSLCAPath'] 
