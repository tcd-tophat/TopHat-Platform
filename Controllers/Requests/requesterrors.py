import exceptions

class RequestError(exceptions.Exception):
	code = 0
	message = None

	def __init__(self, code, message):
		self.message = message
		self.code = code


class NotFound(RequestError):

	def __init__(self, message):
		self.code = 404
		self.message = message


class ServerError(RequestError):

	def __init__(self, message):
		self.code = 500
		self.message = message


class Unauthorised(RequestError):

	def __init__(self, message):
		self.code = 401
		self.message = message


class MethodNotAllowed(RequestError):

	def __init__(self):
		self.code = 405
		self.message = "There is no method available at that URI. Check the documentation."