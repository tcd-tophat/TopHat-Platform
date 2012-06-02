import re
from time import asctime
import domainexception
import urllib2
from jsonparser import JsonParser

# HTTPData takes a HTTP response from a client and provides easy access to it's components.
class HttpData:
	
	_raw_http = None
	_is_json = False
	_parser = None
	_data_path = None
	_status_line = None
	_data_object = None
	_request_type = None
	_parse_error = False

	def __init__(self, _raw_http = None, _is_json = False):

		self._raw_http = _raw_http
		self._is_json = _is_json

		self._parser = JsonParser()

		if _raw_http != None:
			self.parseResponse()
		else:
			raise domainexception.DomainException("HttpData must be initilised with the raw HTTP Response")

	def __str__(self):
		return  str(self._raw_http)

	def parseResponse(self, data = None):
		"""Converts the classes raw http response into it's basic components."""

		if data != None:
			data = data.rstrip()
		else:
			data = self._raw_http.rstrip()

		data = data.split('\n', 1)

		try:
			if self._is_json == True:
				self._data_object = self._parser.getObject(urllib2.unquote(data[1].split('=')[1]))
			else:
				self._data_object = data[1].split('\r\n\r\n')[1]

			self._status_line = data[0].split('\n')[0]
			self._data_path = self._status_line.split()[1]
			self._request_type = self._status_line.split(' ')[0]
		except:
			self._parse_error = True

	# setters #

	def setRawResponse(self, _raw_http):
		"""Changes the current raw response and parses this"""
		self._raw_http = _raw_http

		if self._raw_http != None:
			self.parseResponse()
		else:
			raise domainexception.DomainException("HttpData must be initilised with the raw HTTP Response")


	# getters #

	def parseError(self):
		return self._parse_error

	def getRequestType(self):
		return self._request_type

	def getStatusLine(self):
		return self._status_line

	def getDataObject(self):
		return self._data_object

	def getRawResponse(self):
		return self._raw_http

	def getDataPath(self):
		return  self._data_path