from cherrypy import config as CherryPyConfig, quickstart
from Networking.statuscodes import StatusCodes

class Protocol(BaseProtocol):

	_config = None

	def __init__(self, config):
		super(Protocol, self).__init__(config)
		self._registerStatusCodes()
		

	
	def loop(self):
		from Networking.Protocols.Cherrypy.cherrypyhandler import CherrypyHandler
		quickstart(CherrypyHandler(self))
	def bind(self):

		CherryPyConfig.update({'server.socket_host': self._config.Interface, 
                         'server.socket_port': self._config.Port,
                        }) 

	def _registerStatusCodes(self):
		StatusCodes.NONE = 0
		StatusCodes.OK = 200
		StatusCodes.CREATED = 201
		StatusCodes.BAD_REQUEST = 400
		StatusCodes.UNAUTHORISED = 401
		StatusCodes.FORBIDDEN = 403
		StatusCodes.NOT_FOUND = 404
		StatusCodes.METHOD_NOT_ALLOWED = 405
		StatusCodes.CONFLICT = 409
		StatusCodes.SERVER_ERROR = 500
		StatusCodes.UNIMPLEMENTED = 501