import cherrypy
from Networking.statuscodes import StatusCodes
from Networking.network import Network

class Networking(Network):

	_config = None

	def __init__(self, config):
		self._registerStatusCodes()
		self._config = config

		from tophat import TophatMain

		TophatMain(self._config)

	def _registerStatusCodes(self):
		StatusCodes.NONE = 0
		StatusCodes.OK = 200
		StatusCodes.CREATED = 201
		StatusCodes.UNAUTHORISED = 401
		StatusCodes.NOT_FOUND = 404
		StatusCodes.METHOD_NOT_ALLOWED = 405
		StatusCodes.SERVER_ERROR = 500
		StatusCodes.UNIMPLEMENTED = 501