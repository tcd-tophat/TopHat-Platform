import exceptions

from Networking.statuscodes import StatusCodes as CODE


class RequestError(exceptions.Exception):
	code = CODE.NONE
	message = None

	def __init__(self, code, message):
		self.message = message
		self.code = code


class NotFound(RequestError):

	def __init__(self, message):
		self.code = CODE.NOT_FOUND
		self.message = message


class ServerError(RequestError):

	def __init__(self, message):
		self.code = CODE.SERVER_ERROR
		self.message = message


class Unauthorised(RequestError):

	def __init__(self, message):
		self.code = CODE.UNAUTHORISED
		self.message = message


class MethodNotAllowed(RequestError):

	def __init__(self):
		self.code = CODE.METHOD_NOT_ALLOWED
		self.message = "There is no method available at that URI. Check the documentation."