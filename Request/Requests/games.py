from Request.request import Request
from Request.requesterrors import NotFound, ServerError, Unauthorised, MethodNotAllowed, RequestError
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
		if self.arg is not None:
			try:
				GameMapper = GM.GameMapper()

				if self.arg.isdigit():
					# Get the user by ID
					game = GameMapper.find(self.arg)
				else:
					raise RequestError(CODE.BAD_REQUEST, "Games must bed requested by ID")

				if game is not None:

					gamedict = {
						"id": game.getId(),
						"name": game.getName(),
						"game_type": game.getGameTypeName(),
						"game_type_id": game.getGameTypeId(),
						"time": str(game.getTime()),
						"creator": 
							{	
								"id": game.getCreator().getId(),
								"name": game.getCreator().getName()
							}
					}

					return self._response(gamedict, CODE.OK)
				else:
					raise NotFound("This game does not exist")
			except mdb.DatabaseError, e:
				raise ServerError("Unable to search the game database (%s: %s)" % e.args[0], e.args[1])
		else:
			raise RequestError(CODE.UNIMPLEMENTED, "Getting a list of games is currently unimplemented")

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