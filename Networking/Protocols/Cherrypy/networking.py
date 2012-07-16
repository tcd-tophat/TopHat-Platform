import cherrypy
from Networking.statuscodes import StatusCodes
from Networking.network import Network

class Networking(Network):

	_config = None

	def __init__(self, config):
		self._registerStatusCodes()

		self._config = config

		# This is done here are the _register status cdes method must be called before the handler is imported.
		from Networking.Protocols.Cherrypy.cherrypyhandler import CherrypyHandler

		cherrypy.config.update({'server.socket_host': self._config.Interface, 
                         'server.socket_port': self._config.Port,
                        }) 
		cherrypy.quickstart(CherrypyHandler(self))

	def _registerStatusCodes(self):
		StatusCodes.NONE = 0
		StatusCodes.OK = 200
		StatusCodes.CREATED = 201
		StatusCodes.BAD_REQUEST = 400
		StatusCodes.UNAUTHORISED = 401
		StatusCodes.NOT_FOUND = 404
		StatusCodes.METHOD_NOT_ALLOWED = 405
		StatusCodes.CONFLICT = 409
		StatusCodes.SERVER_ERROR = 500
		StatusCodes.UNIMPLEMENTED = 501