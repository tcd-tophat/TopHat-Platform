from request import Request
from requesterrors import NotFound, ServerError, Unauthorised, MethodNotAllowed

class Users(Request):

	def __init__(self):
		super(Users, self).__init__()
		print "init"

	def _doGet(self, url):
		

	def _doPost(self, url, dataObject):
		self._response.setCode(501)

	def _doPut(self, url, dataObject):
		self._response.setCode(501)

	def _doDelete(self, url):
		self._response.setCode(501)