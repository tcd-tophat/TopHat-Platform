from twisted.internet.protocol import Protocol, Factory
from tophathttpparser import HTTPParser
from dns.resolver import NXDOMAIN, Resolver, query, Timeout as DNSTimeout
from dns import reversename
from Model.tophatclient import TophatClient
from Common.log import LogFile
from Common.date import Timestamp
config=None
class TopHat(Protocol):
	
	def __init__(self, factory):
		self.factory = factory(config)
		client = None
	
	def connectionMade(self):
		
		self.client = TophatClient(transport = self.transport)
		q = Resolver()
		q.lifetime = 2.0
		addr = reversename.from_address(self.transport.getPeer().host)
		try:
				host = str(q.query(addr, 'PTR')[0])
		except NXDOMAIN:
				host = None
		except DNSTimeout:
				host = None
		
		if host is not None:
			
			diagMessage = '%s: connection made from: %s (%s)' % (Timestamp(),host.rstrip('.'), str(self.transport.getPeer().host))
#			self.factory.log.write(diagMessage+'\n')
#			print diagMessage

		else:
			
			diagMessage = '%s: connection made from: %s' % (Timestamp(), str(self.transport.getPeer().host))
#			print diagMessage
#			self.factory.log.write(diagMessage +'\n')
	
	
	def dataReceived(self, data):
		# Basically the main controller for everything to do with data/requests.

		diagMessage =  '%s: received %s' % (Timestamp(), data.rstrip())
#		self.factory.log.write(diagMessage + '\n')
#		print diagMessage
		
		HTTPParser(self, data, self.client)
		
		# not implemented

		if str(self.client.state) == 'get':
			from getrequest import getRequest
			request_value = getRequest(self.client,data)
		
		elif str(self.client.state) == 'put':
			from putrequest import putRequest
			request_value = putRequest(self.client,data, self.factory.LogFilePath)

		elif str(self.client.state) == 'post':
			from postrequest import postRequest
			request_value = postRequest(self.client,data, self.factory.LogFilePath)
		
		elif str(self.client.state) == 'delete':
			from deleterequest import deleteRequest
			request_value = deleteRequest(self.client,data)
		
		elif str(self.client.state) == 'undef':
			self.respondToClient('400 Bad Request')
			self.transport.loseConnection()
			return

		for x in TophatClient:
				if str(x.state) is 'done':
						x.transport.loseConnection()
				x.delete()


		if request_value is -1:
			self.respondToClient('400 Bad Request')
			self.transport.loseConnection()
			return

	def respondToClient (self, messege):
			
#		print '%s: %s' % (Timestamp(), messege)
#		self.factory.log.write('%s: %s' % (Timestamp(), messege) +'\n')
		self.transport.write (messege + '\n\r')
		return



	def connectionLost(self, reason):
		
		address = self.transport.getPeer().host
		q = Resolver()
		q.lifetime = 2.0
		addr = reversename.from_address(address)
		try:
				host = str(q.query(addr, 'PTR')[0])
		except NXDOMAIN:
				host = None
		except DNSTimeout:
				host = None


		
		if host is not None:
			diagMessage = '%s: connection lost from %s (%s): %s' % (Timestamp(),host.rstrip('.'),address,str(reason.getErrorMessage()))
#			self.factory.log.write(diagMessage + '\n')
#			print diagMessage
		
		else:
				pass
#				diagMessage = '%s: connection lost from %s: %s' % (Timestamp(), address, str(reason.getErrorMessage()))
#				self.factory.log.write(diagMessage + '\n')
#				print diagMessage

class TopHatFactory(Factory):
	
	def __init__(self, ConfigObject):
		global config
		config=ConfigObject
		self.LogFilePath = ConfigObject.LogFile
		self.protocal = TopHat
		self.clients = list()
#		self.log = LogFile(self.LogFilePath)
	
	def popClient(self, client):
		
		self.clients.remove(client)
	
	def appendClient(self, client):
		
		self.clients.append(client)
		self.numClients = len(self.clients)
		
	def buildProtocol(self, addr):
		
		return TopHat(TopHatFactory)
