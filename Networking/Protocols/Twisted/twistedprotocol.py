from Networking.protocol import Protocol

class TwistedProtocol(Protocol):

	def __init__(self):
		self._registerStatusCodes()

	def _registerStatusCodes(self):
		from Networking.statuscodes import StatusCodes

		StatusCodes.NONE = 0
		StatusCodes.OK = 200
		StatusCodes.CREATED = 201
		StatusCodes.UNAUTHORISED = 401
		StatusCodes.NOT_FOUND = 404
		StatusCodes.METHOD_NOT_ALLOWED = 405
		StatusCodes.SERVER_ERROR = 500
		StatusCodes.UNIMPLEMENTED = 501