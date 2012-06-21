from abc import abstractmethod, ABCMeta
from requesterrors import ServerErrors

class Request:

	__metaclass__ = ABCMeta

	@abstractmethod
	def __init__(self, response):
		self._response = response
	
	def get(self, data):
		self._url = url

		self._doGet(url)

	def post(self, data):
		self._url = url
		self._dataObject = dataObject

		self._doPost(url, dataObject)

	def put(self, data):
		self._url = url
		self._dataObject = dataObject

		self._doPut(url, dataObject)

	def delete(self, data):
		self._url = url

		self._doDelete(url)

	def __response(self, code, data):
		codeChoices = [200, 201]

		if code not in codeChoices:
			raise ServerError("Unable to build the response")

		info = {}
		info["code"] = code
		info["data"] = data

		return info

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