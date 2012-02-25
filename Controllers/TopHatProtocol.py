from twisted.internet.protocol import Protocol, Factory
from TopHatHTTPParser import HTTPParser
from subprocess import check_output
from dns.resolver import NXDOMAIN, NoAnswer, Resolver, query, Timeout
from dns import reversename
from sys import path
path.append('..')
from Common.Log import LogFile
class TopHat(Protocol):
	def __init__(self, factory):
		self.factory = factory()

	def connectionMade(self):
		self.factory.appendClient(self.transport.getHost().host)
		
		q=Resolver()
		
		q.lifetime=2.0
		
		addr = reversename.from_address(self.transport.getPeer().host)
		
		host = str(q.query(addr, 'PTR')[0])
		
		if host is not None:
			diagMessege = "[" + check_output(['date', '+%T:%D']).rstrip() + ']' + ': connection made from: ' + host.rstrip('.') + ' (' + str(self.transport.getPeer().host)+')'
			self.factory.log.write(diagMessege+'\n')
			print diagMessege
		else:
			diagMessege = "[" + check_output(['date', '+%T:%D']).rstrip() +']'+ ': connection made from: ' + str(self.transport.getPeer().host)  
			print diagMessege
			self.factory.log.write(diagMessege+'\n')
	
	def dataReceived(self, data):
		diagMessege =  "["+ check_output(['date', '+%T:%D']).rstrip() + ']' + ': received ' + data.rstrip()
		self.factory.log.write(diagMessege+'\n')
		print diagMessege
		HTTPParser(self, data)

	def connectionLost(self, reason):
		diagMessege = "[" + check_output(['date', '+%T:%D']).rstrip() +']'+ ': connection lost: '+str(reason.getErrorMessage())
		self.factory.log.write(diagMessege+'\n')
		print diagMessege
class TopHatFactory(Factory):
	log = LogFile('/var/log/tophat/tophat.log')
	protocal = TopHat
	clients = list()
	def popClient(self):
		self.clients.pop()
	def appendClient(self, client):
		self.clients.append(client)
		self.numClients = len(self.clients)
		
	def buildProtocol(self, addr):
		return TopHat(TopHatFactory)
