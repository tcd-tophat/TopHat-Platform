from Request.request import Request
from Request.requesterrors import NotFound, ServerError, BadRequest
from Networking.statuscodes import StatusCodes as CODE
from Model.authentication import require_login

from Model.Mapper.gametypemapper import GameTypeMapper
import MySQLdb as mdb

class Gametypes(Request):

	''' 
		API Documentation
		Documentation for the Core Request of Games is available from the TopHat wiki at:
		http://wiki.tophat.ie/index.php?title=Core_Requests:_Game
	'''

	def __init__(self):
		super(Gametypes, self).__init__()

	@require_login
	def _doGet(self):
		try:
			
			GTM = GameTypeMapper()
			
			if self.arg is not None:
				if self.arg.isdigit():
					# Get the user by ID
					gametype = GTM.find(self.arg)

					if gametype is not None:
						return self._response(gametype.dict(3), CODE.OK)
					else:
						raise NotFound("The specified game type does not exist.")
				else:
					raise BadRequest("Argument provided for this URL is invalid.")
			else:

				offset = 0
				games = GTM.findAll(offset, offset+50)

				if games is None:
					raise NotFound("There are no game types on this system.")

				gameslist = []

				for game in games:
					gameslist.append(game.dict())

				gamedict = {"gametypes":gameslist, "pagination_offset":offset, "max_perpage": 50}

				return self._response(gamedict, CODE.OK)

		except mdb.DatabaseError, e:
			raise ServerError("Unable to search the gametype database (%s: %s)" % e.args[0], e.args[1])