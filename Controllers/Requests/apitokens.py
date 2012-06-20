from Model.Mapper import usermapper as UM
from Model.Mapper import apitokenmapper as ATM
from Common.apikeygen import getKey
from Common.passHash import checkHash

from request import Request
from requesterrors import NotFound, ServerError, Unauthorised, MethodNotAllowed
import MySQLDb as mdb

class Apitokens(Request):

	def __init__(self, response, **kwargs):
		super(Apitokens, self).__init__(response)

	def _doGet(self, url):
		raise MethodNotAllowed()			# method not allowed

	def _doPost(self, url, dataObject):
		response = self._response

		if dataObject.has_key('username') and dataObject.has_key('password'):

			username = dataObject['username']
			password = dataObject['password']

			try:
				UserMapper = UM.UserMapper()
				selectedUser = UserMapper.getUserByEmail(username)
			except mdb.DatabaseError, e:
				raise ServerError("Unable to search the user database (%s: %s)" % e.args[0], e.args[1])

			# check we have a result
			if selectedUser is None:
				raise NotFound("We have no record of a user with the username %s" % username)

			# check password is correct	return corresponding key
			if not checkHash(password, selectedUser.getPassword()):
				raise Unauthorised("Failed to login with that username and password")

			try:
				data = {}
				ATM_ = ATM.ApitokenMapper()
				data["apitoken"] = ATM_.findTokenByUserId(selectUser.getId())

				return self.__response(201, data)

			except mdb.DatabaseError, e:
				raise ServerError("Unable to get API key from the database (%s: %s)" % e.args[0], e.args[1])

		else:
			# Anonymous login
			data = {}
			data["apitoken"] = getKey()

			return self.__response(201, data)

	def _doPut(self, url, dataObject):
		raise MethodNotAllowed()

	def _doDelete(self, url):
		raise MethodNotAllowed()