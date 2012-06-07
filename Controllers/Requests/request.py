from abc import abstractmethod, ABCMeta

class Request:

		__metaclass__=ABCMeta
		
		@abstractmethod
		def __init__(self, response):
				self._response=_response
				self._dataObject = dataObject
		
		@abstractmethod
		def get(self, url):
				self._url = url

		@abstractmethod
		def post(self, url, dataObject):
				self._url = url
				self._dataObject = dataObject


		@abstractmethod
		def put(self, url, dataObject):
				self._url = url
				self._dataObject = dataObject


		@abstractmethod
		def delete(self, url):
				self._url = url