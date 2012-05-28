from encryption import Encryption
from ssl import wrap_socket, SSLSocket

class SSLEncryption(Encryption):
		_securesock=True
		def __init__(self, _sock, **kwargs):
				super(SSLEncryption, self).__init__(_sock)
				try:
						self._keyfile = kwargs['keyfile']
						self._certfile= kwargs['certfile']
						self._ca_certs= kwargs['ca_certs']
				except KeyError:
						raise TypeError('Expected keyfile, certfile and ca_certs got %s instead.' % str(kwargs))
				self._securesock= wrap_socket(self,keyfile=self._keyfile, certfile=self._certfile, server_side=True, ca_certs=self._ca_certs, do_handshake_on_connect=False)

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
				return self._securesock.close()
