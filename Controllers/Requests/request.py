from abc import abstractmethod, ABCMeta

class Request:

	__metaclass__ = ABCMeta

	@abstractmethod
	def __init__(self, response):
		self._response = response
	
	def get(self, url):
		self._url = url

		self._doGet(url)

	def post(self, url, dataObject):
		self._url = url
		self._dataObject = dataObject

		self._doPost(url, dataObject)

	def put(self, url, dataObject):
		self._url = url
		self._dataObject = dataObject

		self._doPut(url, dataObject)

	def delete(self, url):
		self._url = url

		self._doDelete(url)

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