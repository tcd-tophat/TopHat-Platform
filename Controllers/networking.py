from asyncore import dispatcher, dispatcher_with_send
from sys import exit
from threading import Thread
from Queue import Queue, Empty as QueueEmpty
from socket import AF_INET6 as ipv6, SOCK_STREAM as tcp, socket,inet_aton, error as SocketError, timeout as SocketTimeout
from Model.tophatclient import TopHatClient
from Common.config import TopHatConfig
from struct import pack, unpack, error as HeaderFormatError
class Transport(object):
		
		class Peer(object):
				def __init__(self, port, address):
						self.port =port
						self.host =address
		
		def __init__(self, socket,handle):
				#if type(socket) is not type(socket()):
				#		raise TypeError("Expected socket type got %s type instead" % type(socket))
				self.__handle = handle
				self.__sock=socket
		
		def write(self, data):
				try:
						self.__sock.send(data)
				except SocketError:
						return
		
		def loseConnection(self):
				self.__handle.close()
		
		def getPeer(self):
				try:
						tmp=self.__sock.getpeername()
				except SocketError:
					return None
				return Transport.Peer(tmp[1], tmp[0])



class TopHatThread(Thread):

		def __init__(self,queue):
				Thread.__init__(self)
				self.queue=queue
				self.config = TopHatConfig.getConfig()
				self.stop=False
				self.transport=None

		def run(self):
				while not self.stop:
						data = self.queue.get()
						from tophathttpparser import HTTPParser
						self.transport=Transport(data[0],data[2])
						if self.transport is None:
								continue
						client = TopHatClient(transport=self.transport)

						client.transport.loseConnection()
						del client
				return

class TopHatNetwork(dispatcher):
		__workers=[]
		ver=2

		def __init__(self, family, host=None, port=443):

				from sys import exit
				dispatcher.__init__(self)
				self.queue = Queue()
				self.port=port
				self.host=host
				self.config = TopHatConfig.getConfig()

				for x in range(0,self.config.Threads):

						x = TopHatThread(self.queue)
						
						self.__workers.append(x)

						x.daemon=True

						x.start()

				if host is not None:
						try:
								inet_aton(host)
						except SocketError:
								if family is not ipv6:
										exit(1)
								else:
										pass
				self.create_socket(family, tcp)

				self.set_reuse_addr()

				if host is None:
						if family is ipv6:
							self.bind(("::", port))

						else:
							self.bind(("0.0.0.0", port))
				else:
						self.bind((host, 443))
				self.listen(5)
				return

		def handle_accept(self):
				sock, addr = self.accept()
				sock=self.config.EncryptionMethod(sock._sock)
				if not sock.initialized():
						del sock
						return
				client=ClientHandle(sock, self.queue)

		def shutdown(self):
				for x in self.__workers:
						x.stop=True
						del x

				self.close()
				return



class ClientHandle(dispatcher):

		def __init__(self, sock,queue):
				self.sock=sock
				self.queue=queue
				self.sendqueue = Queue()
				dispatcher.__init__(self, sock=sock)
				return

		def handle_read(self):
				try:
						header = self.recv(8)
						try:
												header=unpack("BBHHH", header)
						except HeaderFormatError:
							self.close()
							return 
						ver=header[0]
						
						if TopHatNetwork.ver is not ver:
							self.close()
							return

						opcode=header[1]
						res=header[2]
						datalen=header[3]
						urilen=header[4]
						uri=self.recv(urilen)
						data=self.recv(datalen)
						print "HEADER: %d %d %d %d \nURI: %s\nDATA: %s" % (opcode,res,datalen,urilen,uri,data)



				except SocketTimeout:
						self.close()
						return

				self.queue.put((self.sock,header,self,data,uri))
				return

		def handle_close(self):
		#		my = TopHatClient(transport=Transport(self.sock,self))
		#		if my in TopHatClient:
		#				my.delete()
				return self.close()
	
		def writeable(self): return True

		def readable(self): return True

def respondToClient(transport, data):
		if type(transport) is not Transport:
				raise TypeError('Expected Transport type got %s type instead' % type(transport))
		
		transport.write(data + '\r\n')
		return
