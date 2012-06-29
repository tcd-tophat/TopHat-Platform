from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor
from Networking.statuscodes import StatusCodes

class Networking:

	protocol_handler = None

	def __init__(self, protocol_handler):
		self.protocol_handler = protocol_handler

		self._registerStatusCodes()

		from twistedhandler import TwistedHandler
		root = TwistedHandler(self)
		factory = Site(root)
		reactor.listenTCP(8880, factory)
		reactor.run()

	def getHandler(self):
		return self.protocol_handler

	def _registerStatusCodes(self):
		StatusCodes.NONE = 0
		StatusCodes.OK = 200
		StatusCodes.CREATED = 201
		StatusCodes.UNAUTHORISED = 401
		StatusCodes.NOT_FOUND = 404
		StatusCodes.METHOD_NOT_ALLOWED = 405
		StatusCodes.SERVER_ERROR = 500
		StatusCodes.UNIMPLEMENTED = 501