from request import Request

class Users(Request):

	def __init__(self, _response, **kwargs):
		super(Jsontest, self).__init__(_response)
		print "init"

	def get(self, url):
		super(Jsontest,self).get(url)
		self._response.setCode(501)

	def post(self, url, dataObject):
		super(Jsontest,self).post(url, dataObject)
		self._response.setCode(501)

	def put(self, url, dataObject):
		super(Jsontest,self).put(url, dataObject)
		self._response.setCode(501)

	def delete(self, url):
		super(Jsontest,self).delete(url)
		self._response.setCode(501)