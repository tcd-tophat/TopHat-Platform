from Model.Mapper import usermapper as UM
from Model.Mapper import apitokenmapper as ATM
from Common.apikeygen import getKey
from Common.passHash import checkHash
from Networking.statuscodes import StatusCodes as CODE
from Model.user import User
from Model.apitoken import Apitoken
from Request.request import Request
from Request.requesterrors import NotFound, ServerError, Unauthorised
import MySQLdb as mdb

class Apitokens(Request):

	''' 
		API Documentation
		Documentation for the Core Request of API Tokens is available from the TopHat wiki at:
		http://wiki.tophat.ie/index.php?title=Apitoken
	'''

	def __init__(self):
		super(Apitokens, self).__init__()

	def _doPost(self, dataObject):
		if "email" in dataObject and "password" in dataObject:

			username = dataObject['email']
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
				rdata["user"] = selectedUser.dict(1)

				return self._response(rdata, CODE.CREATED)

			except mdb.DatabaseError, e:
				raise ServerError("Unable to get API key from the database (%s: %s)" % e.args[0], e.args[1])

		else:
			# Anonymous login
			rdata = {}

			token = Apitoken()
			token.setToken(getKey())

			

			blank = User()
			blank.setToken(token)
			token.setUser(blank)

			UserMapper = UM.UserMapper()
			ApitokenMapper = ATM.ApitokenMapper()

			blank.setRegistered(False)

			# Save changes to user
			try:
				UserMapper.insert(blank)

			# handle the possibility the user already exists
			except mdb.IntegrityError, e:
				raise Conflict(CODE.CONFLICT, "A unexpected conflict occurred when trying to create your anonymous login token.")

			# handle all other DB errors
			except mdb.DatabaseError, e:
				raise ServerError("Unable to create user in the database (%s)" % e.args[1])

			# save the apitoken
			try:
				ApitokenMapper.insert(token)
			except mdb.DatabaseError, e:
				raise ServerError("Unable to save apitoken in the database (%s)" % e.args[1])

			rdata["apitoken"] = token.getToken()
			rdata["user"] = blank.dict()

			return self._response(rdata, CODE.CREATED)