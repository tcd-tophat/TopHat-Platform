from request import Request
from Model.authentication import requirelogin

class Jsontest(Request):

	def __init__(self, _response, **kwargs):
		super(Jsontest, self).__init__(_response)

	@requirelogin
	def _doGet(self, url):
		self._response.setCode(200)
		self._response.setData ('{"glossary": {"title": "example glossary","GlossDiv": {"title": "S","GlossList": {"GlossEntry": {"ID": "SGML","SortAs": "SGML","GlossTerm": "Standard Generalized Markup Language","Acronym": "SGML","Abbrev": "ISO 8879:1986","GlossDef": {"para": "A meta-markup language, used to create markup languages such as DocBook.","GlossSeeAlso": ["GML", "XML"]},"GlossSee": "markup"}}}}}')

	def _doPost(self, url, dataObject):
		self._response.setCode(501)

	def _doPut(self, url, dataObject):
		self._response.setCode(501)

	def _doDelete(self, url):
		self._response.setCode(501)