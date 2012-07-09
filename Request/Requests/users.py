from Request.request import Request
from Request.requesterrors import NotFound, ServerError, Unauthorised, MethodNotAllowed, RequestError, BadRequest
from Networking.statuscodes import StatusCodes as CODE
from Model.authentication import requireapitoken
from Common.apikeygen import getKey

from Model.Mapper import usermapper as UM
from Model.Mapper import apitokenmapper as ATM
from Model.user import User
from Model.apitoken import Apitoken
import MySQLdb as mdb

class Users(Request):

	''' 
		API Documentation
		Documentation for the Core Request of Games is available from the TopHat wiki at:
		http://wiki.tophat.ie/index.php?title=Core_Requests:_Users
	'''

	def __init__(self):
		super(Users, self).__init__()

	@requireapitoken
	def _doGet(self):
		if self.arg is not None:
			try:
				UserMapper = UM.UserMapper()

				if self.arg.isdigit():
					# Get the user by ID
					user = UserMapper.find(self.arg)
				else:
					# Get the user by E-mail
					user = UserMapper.getUserByEmail(self.arg)

				if user is not None:
					return self._response(user.dict(), CODE.OK)
				else:
					raise NotFound("This user does not exist")

			except mdb.DatabaseError, e:
				raise ServerError("Unable to search the user database (%s: %s)" % e.args[0], e.args[1])
		else:
			raise RequestError(CODE.UNIMPLEMENTED, "Getting a list of users is currently unimplemented")

	@requireapitoken
	def _doPost(self, dataObject):

		if "email" in dataObject and "password" in dataObject:
			try:

				UserMapper = UM.UserMapper()
				ApitokenMapper = ATM.ApitokenMapper()

				user = User()

				user.setEmail(dataObject["email"])
				user.setPreHash(dataObject["password"])

				UserMapper.insert(user)

				# Retrieve user with ID this time
				user = UserMapper.getUserByEmail(dataObject["email"])

				token = Apitoken()

				token.setUser(user)
				token.setToken(getKey())

				ApitokenMapper.insert(token)

				return self._response(token.dict(), CODE.CREATED)
				
			except mdb.DatabaseError, e:
				raise ServerError("Unable to search the user database (%s)" % e.args[1])
		else:
			raise BadRequest("Required params email and password not sent")

	@requireapitoken
	def _doPut(self, dataObject):
		return self._response({}, CODE.UNIMPLEMENTED)

	@requireapitoken
	def _doDelete(self):
		if self.arg is not None:
			try:
				UserMapper = UM.UserMapper()

				if self.arg.isdigit():
					# Get the user by ID
					user = UserMapper.find(self.arg)
				else:
					# Get the user by E-mail
					user = UserMapper.getUserByEmail(self.arg)
				if user is not None:
					UserMapper.delete(user)
					return self._response({"message": "User Deleted Successfully."}, CODE.OK)
				else:
					raise NotFound("This user does not exist")
			except mdb.DatabaseError, e:
				raise ServerError("Unable to search the user database (%s: %s)" % e.args[0], e.args[1])
		else:
			raise MethodNotAllowed("You must provide the user ID or user EMAIL of the user to be deleted")

		return self._response({}, CODE.UNIMPLEMENTED)