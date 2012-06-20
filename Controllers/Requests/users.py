from request import Request

class Users(Request):

	def __init__(self, _response, **kwargs):
		super(Jsontest, self).__init__(_response)
		print "init"

	def _doGet(self, url):
		self._response.setCode(501)

	def _doPost(self, url, dataObject):
		self._response.setCode(501)

	def _doPut(self, url, dataObject):
		self._response.setCode(501)

	def _doDelete(self, url):
		self._response.setCode(501)