from abc import abstractmethod, ABCMeta
from requesterrors import ServerError

class Request:

	__metaclass__ = ABCMeta

	@abstractmethod
	def __init__(self):
		pass
	
	def get(self, url):
		self._url = url

		return self._doGet(url)

	def post(self, url, dataObject):
		self._url = url
		self._dataObject = dataObject

		return self._doPost(url, dataObject)

	def put(self, url, dataObject):
		self._url = url
		self._dataObject = dataObject

		return self._doPut(url, dataObject)

	def delete(self, url):
		self._url = url

		return self._doDelete(url)

	def _response(self, code, data):
		codeChoices = [200, 201]

		if code not in codeChoices:
			raise ServerError("Unable to build the response, invalid status code")

		response = {}
		response["code"] = code
		response["data"] = data

		return response

	@abstractmethod
	def _doGet(self, url):
		pass

	@abstractmethod
	def _doPost(self, url, dataObject):
		pass

	@abstractmethod
	def _doPut(self, url, dataObject):
		pass

	@abstractmethod
	def _doDelete(self, url):
		pass