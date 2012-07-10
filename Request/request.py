from abc import abstractmethod, ABCMeta
from requesterrors import ServerError, MethodNotAllowed, Unauthorised
from response import Response

from Networking.statuscodes import StatusCodes as CODE
from Model.Mapper import apitokenmapper as ATM
import MySQLdb as mdb

class Request:

	__metaclass__ = ABCMeta

	user = None

	@abstractmethod
	def __init__(self):
		pass

	def get(self):
		return self._doGet()

	def post(self, data):
		return self._doPost(data)

	def put(self, data):
		return self._doPut(data)

	def delete(self):
		return self._doDelete()

	def setArg(self, arg):
		self.arg = arg

	# This method auto loads in a user if they have supplied an APIkey with their request. This makes it easier for the developer to manipulate and respond.
	def setApiKey(self, key):
		self.key = key

		if key is not None:
			try:
				ATM_ = ATM.ApitokenMapper()
				apikey = ATM_.findUserByTokenId(key)
				self.user = apikey.getUser()
			except mdb.DatabaseError, e:
				raise ServerError("Unable to search the user database (%s)" % e.args[1])
			except:
				raise Unauthorised("An invalid API token was supplied.")

	def _response(self, data, code=CODE.OK):
		return Response(data, code)

	# Functions to be overloaded by child classes
	# otherwise they raise a method not allowed exception
	def _doGet(self):
		raise MethodNotAllowed()			# method not allowed

	def _doPost(self, data):
		raise MethodNotAllowed()			# method not allowed

	def _doPut(self, data):
		raise MethodNotAllowed()			# method not allowed
	
	def _doDelete(self):
		raise MethodNotAllowed()			# method not allowed