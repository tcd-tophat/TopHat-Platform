from twisted.internet.protocol import Protocol, Factory
from tophathttpparser import HTTPParser
from subprocess import check_output
from dns.resolver import NXDOMAIN, NoAnswer, Resolver, query, Timeout
from dns import reversename
from Model.tophatclient import TophatClient
from Common.log import LogFile
import getrequest, postrequest, putrequest, deleterequest
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
		
		if host is not None:
			
			diagMessage = '[' + check_output(['date', '+%T:%D']).rstrip() + ']' + ': connection made from: ' + host.rstrip('.') + ' (' + str(self.transport.getPeer().host)+')'
			self.factory.log.write(diagMessage+'\n')
			print diagMessage

		else:
			
			diagMessage = '[' + check_output(['date', '+%T:%D']).rstrip() + ']' + ': connection made from: ' + str(self.transport.getPeer().host)  
			print diagMessage
			self.factory.log.write(diagMessage +'\n')
	
	
	def dataReceived(self, data):
		# Basically the main controller for everything to do with data/requests.

		diagMessage =  '[' + check_output(['date', '+%T:%D']).rstrip() + ']' + ': received ' + data.rstrip()
		self.factory.log.write(diagMessage + '\n')
		#print diagMessage
		
		HTTPParser(self, data, self.client)
		
		# not implemented

		if str(self.client.state) == 'get':
			from getrequest import getRequest
			request_value = getRequest(self.client,data)
		
		elif str(self.client.state) == 'put':
			from putrequest import putRequest
			request_value = putRequest(self.client,data)

		elif str(self.client.state) == 'post':
			from postrequest import postRequest
			request_value = postRequest(self.client,data)
		
		elif str(self.client.state) == 'delete':
			from deleterequest import deleteRequest
			request_value = deleteRequest(self.client,data)
		
		elif str(self.client.state) == 'undef':
			self.respondToClient('400 Bad Request')
			return

		if request_value is -1:
			self.respondToClient('400 Bad Request')
			return

	def respondToClient (self, message):

		print '['+ check_output(['date', '+%T:%D']).rstrip() + ']: ' + message
		self.factory.log.write('['+ check_output(['date', '+%T:%D']).rstrip() + ']:' + message)
		self.transport.write (message + '\n\r')
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


		
		if host is not None:
			diagMessage = '[' + check_output(['date', '+%T:%D']).rstrip() + ']' + ': connection lost from ' + host.rstrip('.') + ' (' + address + ')' + ': '+ str(reason.getErrorMessage())
			self.factory.log.write(diagMessage + '\n')
			print diagMessage
		
		else:
				diagMessage = '[' + check_output(['date', '+%T:%D']).rstrip() + ']' + ': connection lost from ' + address + ': ' + str(reason.getErrorMessage())
				self.factory.log.write(diagMessage + '\n')
				print diagMessage

class TopHatFactory(Factory):
	
	def __init__(self, ConfigObject):
		global config
		config=ConfigObject
		self.LogFilePath = ConfigObject.LogFile
		self.protocal = TopHat
		self.clients = list()
		self.log = LogFile(self.LogFilePath)
	
	def popClient(self, client):
		
		self.clients.remove(client)
	
	def appendClient(self, client):
		
		self.clients.append(client)
		self.numClients = len(self.clients)
		
	def buildProtocol(self, addr):
		
		return TopHat(TopHatFactory)
