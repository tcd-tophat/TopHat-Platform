import cherrypy
from Networking.statuscodes import StatusCodes
from Networking.network import Network

class Networking(Network):

	def __init__(self):
		self._registerStatusCodes()

		from tophat import TophatMain

		from Common.config import TopHatConfig
		kwargs = {"path":"config.py"}

		TophatMain(TopHatConfig(**kwargs))

	def _registerStatusCodes(self):
		StatusCodes.NONE = 0
		StatusCodes.OK = 200
		StatusCodes.CREATED = 201
		StatusCodes.UNAUTHORISED = 401
		StatusCodes.NOT_FOUND = 404
		StatusCodes.METHOD_NOT_ALLOWED = 405
		StatusCodes.SERVER_ERROR = 500
		StatusCodes.UNIMPLEMENTED = 501