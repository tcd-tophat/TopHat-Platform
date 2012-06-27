from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor

from twistedhandler import TwistedHandler

class Networking:

	protocol_handler = None

	def __init__(self, protocol_handler):
		self.protocol_handler = protocol_handler

		root = TwistedHandler(self)
		factory = Site(root)
		reactor.listenTCP(8880, factory)
		#reactor.listenSSL(self.config, factory, ssl.DefaultOpenSSLContextFactory( self.config.SSLKeyPath, self.config.SSLCertPath))
		reactor.run()

	def getHandler(self):
		return self.protocol_handler