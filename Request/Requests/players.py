from Request.request import Request
from Request.requesterrors import NotFound, ServerError, Unauthorised, MethodNotAllowed, RequestError, BadRequest
from Networking.statuscodes import StatusCodes as CODE
from Model.authentication import requireapitoken

from Model.Mapper import usermapper as UM
from Model.Mapper import gamemapper as GM
from Model.Mapper import playermapper as PM
import MySQLdb as mdb

# Decorator
from Model.authentication import requireapitoken

class Players(Request):

	''' 
		API Documentation
		Documentation for the Core Request of Games is available from the TopHat wiki at:
		http://wiki.tophat.ie/index.php?title=Core_Requests:_Players
	'''

	def __init__(self):
		super(Players, self).__init__()

	@requireapitoken
	def _doGet(self):
		try:
			
			PlayerMapper = PM.PlayerMapper()
			
			if self.arg is not None:
				if self.arg.isdigit():
					# Get the user by ID
					player = PlayerMapper.find(self.arg)
				else:
					raise BadRequest("Games must be requested by ID")

				if player is not None:
					return self._response(player.dict(), CODE.OK)
				else:
					raise NotFound("This player does not exist")
			
			else:

				offset = 0
				players = PlayerMapper.findAll(offset, offset+50)

				playerslist = []

				for player in players:
					playerslist.append(player.dict())

				playerslist = {"players":playerslist, "pagination_offset":offset, "max_perpage": 50}

				return self._response(playerslist, CODE.OK)

		except mdb.DatabaseError, e:
				raise ServerError("Unable to search the player database (%s: %s)" % e.args[0], e.args[1])

	@requireapitoken
	def _doPost(self, dataObject):
		return self._response({}, CODE.UNIMPLEMENTED)

	@requireapitoken
	def _doPut(self, dataObject):
		return self._response({}, CODE.UNIMPLEMENTED)

	@requireapitoken
	def _doDelete(self):
		return self._response({}, CODE.UNIMPLEMENTED)