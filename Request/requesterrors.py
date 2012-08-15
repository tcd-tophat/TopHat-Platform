import exceptions

from Networking.statuscodes import StatusCodes as CODE


class RequestError(exceptions.Exception):
	"""Base request exception class"""

	code = CODE.NONE
	message = None

	def __init__(self, code, message):
		self.message = message
		self.code = code


class BadRequest(RequestError):
	"""HTTP 400 - The request cannot be fulfilled due to bad syntax."""

	def __init__(self, message):
		self.code = CODE.BAD_REQUEST
		self.message = message


class NotFound(RequestError):
	"""
		HTTP 404
		The requested resource could not be found but may be available again 
		in the future. Subsequent requests by the client are permissible.
	"""

	def __init__(self, message):
		self.code = CODE.NOT_FOUND
		self.message = message


class ServerError(RequestError):
	"""HTTP 500 - Internal Server Error"""

	def __init__(self, message):
		self.code = CODE.SERVER_ERROR
		self.message = message


class Unauthorised(RequestError):
	"""HTTP 401 - Specifically for use when authentication is required and has failed or has not yet been provided."""

	def __init__(self, message = None):
		self.code = CODE.UNAUTHORISED

		if message is None:
			self.message = "You must be authenticated in order to use this resource."
		else:
			self.message = message

class Forbidden(RequestError):
	"""
		HTTP 403
		The request was a valid request, but the server is refusing to respond to it.
		Unlike an Unauthorized response, authenticating will make no difference.
		Where authentication is required, this commonly means that the provided 
		credentials were successfully authenticated but that the credentials still 
		do not grant the client permission to access the resource
	"""

	def __init__(self):
		self.code = CODE.FORBIDDEN
		self.message = "Forbidden; you cannot access that resource without higher priviledges"

class MethodNotAllowed(RequestError):
	"""HTTP 405 - A request was made of a resource using a request method not supported by that resource"""

	def __init__(self):
		self.code = CODE.METHOD_NOT_ALLOWED
		self.message = "There is no method available at that URI. Check the documentation."

class Conflict(RequestError):
	"""HTTP 409"""

	def __init__(self, message):
		self.code = CODE.CONFLICT
		self.message = message