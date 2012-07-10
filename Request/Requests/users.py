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
		try:
			UserMapper = UM.UserMapper()

			if self.arg is not None:

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

			else:
				offset = 0
				users = UserMapper.findAll(offset, offset+50)

				userslist = []

				for user in users:
					userslist.append(user.dict())

				userslist = {"users":userslist, "pagination_offset":offset, "max_perpage": 50}

				return self._response(userslist, CODE.OK)

		except mdb.DatabaseError, e:
			raise ServerError("Unable to search the user database (%s: %s)" % e.args[0], e.args[1])

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

		if "name" in dataObject or "email" in dataObject or "photo" in dataObject:
			try:

				UserMapper = UM.UserMapper()

				if self.arg.isdigit():
					# Get the user by ID
					user = UserMapper.find(self.arg)
				else:
					# Get the user by E-mail
					user = UserMapper.getUserByEmail(self.arg)

				if user is not None:
					
					if "name" in dataObject:
						user.setName(dataObject["name"])
					
					if "email" in dataObject:
						user.setEmail(dataObject["email"])

					if "photo" in dataObject:
						user.setPhoto(dataObject["photo"])

					UserMapper.update(user)

					return self._response(user.dict(), CODE.CREATED)
				else:
					raise NotFound("This user does not exist")
				
			except mdb.DatabaseError, e:
				raise ServerError("Unable to search the user database (%s)" % e.args[1])
		else:
			raise BadRequest("The minimum required fields were not provided, which include but are not limited to 'name', 'email' and 'photo'.")

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