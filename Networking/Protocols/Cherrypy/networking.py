import cherrypy
from Networking.statuscodes import StatusCodes
from Networking.network import Network

class Networking(Network):

	def __init__(self):
		self._registerStatusCodes()

		from Networking.Protocols.Cherrypy.cherrypyhandler import CherrypyHandler

		cherrypy.config.update({'server.socket_host': '127.0.0.1', 
                         'server.socket_port': 8880,
                        }) 
		cherrypy.quickstart(CherrypyHandler(self))

	def _registerStatusCodes(self):
		StatusCodes.NONE = 0
		StatusCodes.OK = 200
		StatusCodes.CREATED = 201
		StatusCodes.UNAUTHORISED = 401
		StatusCodes.NOT_FOUND = 404
		StatusCodes.METHOD_NOT_ALLOWED = 405
		StatusCodes.SERVER_ERROR = 500
		StatusCodes.UNIMPLEMENTED = 501