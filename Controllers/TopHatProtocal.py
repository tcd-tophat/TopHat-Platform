from twisted.internet.protocol import Protocol, Factory
from TopHatHTTPParser import HTTPParser
from subprocess import check_output
from dns.resolver import NXDOMAIN, NoAnswer, Resolver, query, Timeout
from dns import reversename
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
			print "[", check_output((['date', '+%T:%D'])).rstrip() + ': connection made from: ' + host.rstrip('.') + ' (', self.transport.getPeer().host,')'+ ']'
		else:
			print "[", check_output((['date', '+%T:%D'])).rstrip() + ': connection made from: ', self.transport.getPeer().host, ']'
	def dataReceived(self, data):
		print "[", check_output((['date', '+%T:%D'])).rstrip() + ': received', data.rstrip() + ']'
		HTTPParser(self, data)
	def connectionLost(self, reason):
		print "[", check_output((['date', '+%T:%D'])).rstrip() + ': connection lost: ',reason.getErrorMessage() ,']'
class TopHatFactory(Factory):
	protocal = TopHat
	clients = list()
	def popClient(self):
		self.clients.pop()
	def appendClient(self, client):
		self.clients.append(client)
		self.numClients = len(self.clients)
		
	def buildProtocol(self, addr):
		return TopHat(TopHatFactory)
