from Model.Mapper import usermapper as UM
from Model.Mapper import apitokenmapper as ATM
from Common.apikeygen import getKey
from Common.passHash import checkHash
from Networking.statuscodes import StatusCodes as CODE

from Request.request import Request
from Request.requesterrors import NotFound, ServerError, Unauthorised, MethodNotAllowed
import MySQLdb as mdb

class Apitokens(Request):

	def __init__(self):
		super(Apitokens, self).__init__()

	def _doPost(self, dataObject):
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

			# get API token from the database and return it
			try:
				rdata = {}
				ATM_ = ATM.ApitokenMapper()
				
				rdata["apitoken"] = ATM_.findTokenByUserId(selectedUser.getId()).getToken()

				return self._response(rdata, CODE.CREATED)

			except mdb.DatabaseError, e:
				raise ServerError("Unable to get API key from the database (%s: %s)" % e.args[0], e.args[1])

		else:
			# Anonymous login
			rdata = {}
			rdata["apitoken"] = getKey()

			return self._response(rdata, CODE.CREATED)