from Request.request import Request
from Request.requesterrors import NotFound, ServerError, Unauthorised, MethodNotAllowed, RequestError
from Networking.statuscodes import StatusCodes as CODE
from Model.authentication import requireapitoken

from Model.Mapper import usermapper as UM
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

					userdict = {
						"id": user.getId(),
						"name": user.getName(),
						"email": user.getEmail(),
						"joined_games": []
					}

					return self._response(userdict, CODE.OK)
				else:
					raise NotFound("This user does not exist")
			except mdb.DatabaseError, e:
				raise ServerError("Unable to search the user database (%s: %s)" % e.args[0], e.args[1])
		else:
			raise RequestError(CODE.UNIMPLEMENTED, "Getting a list of users is currently unimplemented")

		return self._response({}, CODE.UNIMPLEMENTED)

	@requireapitoken
	def _doPost(self, dataObject):
		return self._response({}, CODE.UNIMPLEMENTED)

	@requireapitoken
	def _doPut(self, dataObject):
		return self._response({}, CODE.UNIMPLEMENTED)

	@requireapitoken
	def _doDelete(self):
		return self._response({}, CODE.UNIMPLEMENTED)