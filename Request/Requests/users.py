from Request.request import Request
from Request.requesterrors import NotFound, ServerError, Unauthorised, MethodNotAllowed, BadRequest, Forbidden, Conflict
from Networking.statuscodes import StatusCodes as CODE
from Model.authentication import require_login, require_super_user
from Common.apikeygen import getKey
from Common.utils import checkEmail

from Model.Mapper import usermapper as UM
from Model.Mapper import apitokenmapper as ATM
from Model.user import User
from Model.apitoken import Apitoken
import MySQLdb as mdb

class Users(Request):

	''' 
		API Documentation
		Documentation for the Core Request of Users is available from the TopHat wiki at:
		http://wiki.tophat.ie/index.php?title=Core_Requests:_Users
	'''

	def __init__(self):
		super(Users, self).__init__()

	@require_login
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

				if user is None:
					raise NotFound("This user does not exist")

				if self.user.accessLevel("super_user") or self.user.getId() == user.getId():
					return self._response(user.dict(2), CODE.OK)
				else:
					raise Forbidden()

			else:
				if self.user.accessLevel("super_user"):
					offset = 0
					users = UserMapper.findAll(offset, offset+50)

					userslist = []

					for user in users:
						userslist.append(user.dict(2))

					userslist = {"users":userslist, "pagination_offset":offset, "max_perpage": 50}

					return self._response(userslist, CODE.OK)
				else:
					raise Forbidden()

		except mdb.DatabaseError, e:
			raise ServerError("Unable to search the user database (%s: %s)" % (e.args[0], e.args[1]))

	def _doPost(self, dataObject):

		if "email" in dataObject and "password" in dataObject:
			UserMapper = UM.UserMapper()
			ApitokenMapper = ATM.ApitokenMapper()

			# Build user and token objects
			user = User()

			if not checkEmail(dataObject["email"]):
				raise BadRequest("The e-mail supplied was invalid.")

			user.setEmail(dataObject["email"])
			user.setPreHash(dataObject["password"])
			user.setRegistered(True)

			token = Apitoken()

			token.setUser(user)
			token.setToken(getKey())

			# Save changes to user
			try:
				UserMapper.insert(user)

			# handle the possibility the user already exists
			except mdb.IntegrityError, e:
				raise Conflict("A user with that e-mail address exists already.")

			# handle all other DB errors
			except mdb.DatabaseError, e:
				raise ServerError("Unable to create user in the database (%s)" % e.args[1])

			# save the apitoken
			try:
				ApitokenMapper.insert(token)
			except mdb.DatabaseError, e:
				raise ServerError("Unable to save apitoken in the database (%s)" % e.args[1])

			return self._response(token.dict(2), CODE.CREATED)	
		else:
			raise BadRequest("Required params email and password not sent")

	@require_login
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
					if self.user.getId() is user.getId() or self.user.accessLevel("super_user"):
						if "name" in dataObject:
							user.setName(dataObject["name"])
						
						if "email" in dataObject:
							user.setEmail(dataObject["email"])

						if "photo" in dataObject:
							user.setPhoto(dataObject["photo"])

						UserMapper.update(user)

						return self._response(user.dict(), CODE.CREATED)
					else:
						raise Forbidden()
				else:
					raise NotFound("This user does not exist")
				
			except mdb.DatabaseError, e:
				raise ServerError("Unable to search the user database (%s)" % e.args[1])
		else:
			raise BadRequest("The minimum required fields were not provided, which include but are not limited to 'name', 'email' and 'photo'.")

	@require_login
	def _doDelete(self):
		if self.arg is None:
			raise MethodNotAllowed("You must provide the user ID or user EMAIL of the user to be deleted")
		
		# get the user if it exists
		try:
			UserMapper = UM.UserMapper()

			if self.arg.isdigit():
				user = UserMapper.find(self.arg)
			else:
				# Get the user by E-mail
				user = UserMapper.getUserByEmail(self.arg)
		except mdb.DatabaseError, e:
			raise ServerError("Unable to search the user database (%s: %s)" % e.args[0], e.args[1])

		if user is None:
			raise NotFound("There is no user identified by %s" % self.arg)

		# check user has the priviledges
		if not self.user.getId() is user.getId() and not self.user.accessLevel('delete_users'):
			raise Forbidden()

		# delete the user from the data base
		result = UserMapper.delete(user)

		if result:
			return self._response({"message": "User Deleted Successfully."}, CODE.OK)
		else:
			raise ServerError("Unable to delete the user")
			
