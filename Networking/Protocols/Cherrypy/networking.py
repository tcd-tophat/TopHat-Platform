import cherrypy
from Networking.statuscodes import StatusCodes

class Networking:

	protocol_handler = None

	def __init__(self, protocol_handler):
		self.protocol_handler = protocol_handler

		self._registerStatusCodes()

		from Networking.Protocols.Cherrypy.cherrypyhandler import CherrypyHandler

		cherrypy.config.update({'server.socket_host': '127.0.0.1', 
                         'server.socket_port': 8880,
                        }) 
		cherrypy.quickstart(CherrypyHandler(self))

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