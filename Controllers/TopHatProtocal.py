from twisted.internet.protocol import Protocol, Factory
from subprocess import check_output
import inspect
class TopHat(Protocol):
	def __init__(self, factory):
		self.factory = factory()

	def connectionMade(self):
		self.factory.appendClient(self.transport.getHost().host)
		print "[", check_output((['date', '+%T:%D'])).rstrip() + ': connection made from: ', self.transport.getHost().host, ']'
	def dataReceived(self, data):
		print "[", check_output((['date', '+%T:%D'])).rstrip() + ': recieved', data.rstrip() + ']'
		self.transport.write(str(self.factory.numClients) + '\r\n')
	def connectionLost(self, reason):
		print "[", check_output((['date', '+%T:%D'])).rstrip() + ': connection lost: ',reason.getErrorMessage() ,']'
class TopHatFactory(Factory):
	protocal = TopHat
	clients = list()
	def appendClient(self, client):
		self.clients.append(client)
		self.numClients = len(self.clients)
		
	def buildProtocol(self, addr):
		return TopHat(TopHatFactory)
