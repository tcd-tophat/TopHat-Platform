from request import Request
from Model.authentication import requirelogin

class Jsontest(Request):

		def __init__(self, _response, **kwargs):
				super(Jsontest, self).__init__(_response)

		@requirelogin
		def get(self, url):
				super(Jsontest,self).get(url)
				self._response.setCode(200)
				self._response.setData ('{"glossary": {"title": "example glossary","GlossDiv": {"title": "S","GlossList": {"GlossEntry": {"ID": "SGML","SortAs": "SGML","GlossTerm": "Standard Generalized Markup Language","Acronym": "SGML","Abbrev": "ISO 8879:1986","GlossDef": {"para": "A meta-markup language, used to create markup languages such as DocBook.","GlossSeeAlso": ["GML", "XML"]},"GlossSee": "markup"}}}}}')

		def post(self, url, dataObject):
				super(Jsontest,self).post(url, dataObject)
				self._response.setCode(501)

		def put(self, url, dataObject):
				super(Jsontest,self).put(url, dataObject)
				self._response.setCode(501)

		def delete(self, url):
				super(Jsontest,self).delete(url)
				self._response.setCode(501)