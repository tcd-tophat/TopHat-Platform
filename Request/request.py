from abc import abstractmethod, ABCMeta
from requesterrors import ServerError
from response import Response

from Networking.statuscodes import StatusCodes as CODE

class Request:

	__metaclass__ = ABCMeta

	@abstractmethod
	def __init__(self):
		pass
	
	def get(self, data):
		return self._doGet(data)

	def post(self, data):
		return self._doPost(data)

	def put(self, data):
		return self._doPut(data)

	def delete(self, data):
		return self._doDelete(data)

	def _response(self, data, code=CODE.OK):
		return Response(data, code)

	@abstractmethod
	def _doGet(self, data):
		pass

	@abstractmethod
	def _doPost(self, data):
		pass

	@abstractmethod
	def _doPut(self, data):
		pass

	@abstractmethod
	def _doDelete(self, data):
		pass