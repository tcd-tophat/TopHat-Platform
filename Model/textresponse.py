import re
from time import asctime
import domainexception
from jsonencoder import JsonEncoder

class TextResponse:

	_code = 404
	_data = None

	_errorCodes = None

	json = None
	
	def __init__(self, _code = None, _object = None):

		self._errorCodes = dict({ 200: "OK", 201: "Created", 202:"Accepted", 204: "No Content", 400:"Bad Request", 401:"Unauthorized", 403:"Forbidden", 404:"Not Found", 500:"Internal Server Error", 501:"Not Implemented", 503:"Service Unavailable", 504:"Gateway Timeout"})

		if _code != None:
			self.setCode(_code)
		
		if _object != None:
			self.json = JsonEncoder()
			self._data = self.json.toJson(_object)



	def __str__(self):
		return  " " + str(self._code) + " " + str(self._data)

	def constructStringResponse(self):
		if (self._code != None and self._data != None ):
				return '%s\n\r%s\n\r' % (self.getCode(), self.getData())
		elif ( self._code != None and self._data == None):
				return '%s\n\r' % (self.getCode())
		else:
				raise domainexception.DomainException("Response code or data is missing.")

	def sendResponse(self, socket):
		ver=2
		opcode=0
		res=0
		urilen=len('')
		datalen=len(self.getData())
		header=pack("BBHHH", ver, opcode, res, datalen, urilen)
		socket.write(header)
		socket.write('')
		socket.write(self.getData())


	# setters #

	def setCode(self, _code):
		if self._errorCodes.has_key(_code):
			self._code = _code
		else:
			raise domainexception.DomainException("Given response code '"+str(_code)+"' is not supported by the TopHat platform HttpLib.")

	def setData(self, _data):
		self._data = _data

	def setObject(self, _object):
		self._data = self.json.toJson(_object)


	# getters #

	def getCode(self):
		return self._code

	def getData(self):
		return self._data