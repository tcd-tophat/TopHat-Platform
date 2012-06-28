from abc import abstractmethod, ABCMeta
from requesterrors import ServerError, MethodNotAllowed
from response import Response

from Networking.statuscodes import StatusCodes as CODE

class Request:

	__metaclass__ = ABCMeta

	@abstractmethod
	def __init__(self):
		pass
	
	def get(self):
		return self._doGet()

	def post(self, data):
		return self._doPost(data)

	def put(self, data):
		return self._doPut(data)

	def delete(self):
		return self._doDelete()

	def _response(self, data, code=CODE.OK):
		return Response(data, code)

	# Functions to be overloaded by child classes
	# otherwise they raise a method not allowed exception
	def _doGet(self):
		raise MethodNotAllowed()			# method not allowed

	def _doPost(self, data):
		raise MethodNotAllowed()			# method not allowed

	def _doPut(self, data):
		raise MethodNotAllowed()			# method not allowed
	
	def _doDelete(self):
		raise MethodNotAllowed()			# method not allowed