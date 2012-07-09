from Request.request import Request
from Request.requesterrors import NotFound, ServerError, Unauthorised, MethodNotAllowed, RequestError, BadRequest
from Networking.statuscodes import StatusCodes as CODE
from Model.authentication import requireapitoken

from Model.Mapper import usermapper as UM
from Model.Mapper import gamemapper as GM
import MySQLdb as mdb

class Games(Request):

	''' 
		API Documentation
		Documentation for the Core Request of Games is available from the TopHat wiki at:
		http://wiki.tophat.ie/index.php?title=Core_Requests:_Game
	'''

	def __init__(self):
		super(Games, self).__init__()

	@requireapitoken
	def _doGet(self):
		try:
			
			GameMapper = GM.GameMapper()
			
			if self.arg is not None:
				if self.arg.isdigit():
					# Get the user by ID
					game = GameMapper.find(self.arg)
				else:
					raise BadRequest("Games must be requested by ID")

				if game is not None:
					return self._response(game.dict(), CODE.OK)
				else:
					raise NotFound("There is no game identified by the number %i" % self.arg)
			
			else:

				offset = 0
				games = GameMapper.findAll(offset, offset+50)

				gameslist = []

				for game in games:
					gameslist.append(game.dict())

				gamedict = {"games":gameslist, "pagination_offset":offset, "max_perpage": 50}

				return self._response(gamedict, CODE.OK)

		except mdb.DatabaseError, e:
			raise ServerError("Unable to search the game database (%s: %s)" % e.args[0], e.args[1])


	@requireapitoken
	def _doPost(self, dataObject):
		return self._response({}, CODE.UNIMPLEMENTED)

	@requireapitoken
	def _doPut(self, dataObject):
		return self._response({}, CODE.UNIMPLEMENTED)

	@requireapitoken
	def _doDelete(self):
		return self._response({}, CODE.UNIMPLEMENTED)