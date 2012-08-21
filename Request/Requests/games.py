from Request.request import Request
from Request.requesterrors import NotFound, ServerError, BadRequest, Forbidden
from Networking.statuscodes import StatusCodes as CODE
from Model.authentication import require_login

from Model.Mapper.usermapper import UserMapper
from Model.Mapper.gamemapper import GameMapper
from Model.Mapper.gametypemapper import GameTypeMapper
from Model.game import Game
import MySQLdb as mdb

class Games(Request):

	''' 
		API Documentation
		Documentation for the Core Request of Games is available from the TopHat wiki at:
		http://wiki.tophat.ie/index.php?title=Core_Requests:_Game
	'''

	def __init__(self):
		super(Games, self).__init__()

	@require_login
	def _doGet(self):
		try:
			
			GM = GameMapper()
			
			if self.arg is not None:
				if self.arg.isdigit():
					# Get the user by ID
					game = GM.find(self.arg)
				elif self.arg == "types":
					return self._response({}, CODE.UNIMPLEMENTED)
				else:
					raise BadRequest("Games must be requested by ID")

				if game is not None:
					return self._response(game.dict(3), CODE.OK)
				else:
					raise NotFound("There is no game identified by the number %s" % self.arg)
			
			else:

				offset = 0
				games = GM.findAll(offset, offset+50)

				if games is None:
					raise NotFound("There are no games on this system.")

				gameslist = []

				for game in games:
					gameslist.append(game.dict(2))

				gamedict = {"games":gameslist, "pagination_offset":offset, "max_perpage": 50}

				return self._response(gamedict, CODE.OK)

		except mdb.DatabaseError, e:
			raise ServerError("Unable to search the game database (%s: %s)" % e.args[0], e.args[1])


	@require_login
	def _doPost(self, dataObject):

		# The game creation should have no arguments.
		if self.arg is not None:
			return self._response({}, CODE.UNIMPLEMENTED)

		if "name" and "game_type_id" in dataObject:
			try:
				GTM = GameTypeMapper()

				if dataObject["game_type_id"] is not None and dataObject["game_type_id"].isdigit():
					# Get the user by ID
					gametype = GTM.find(dataObject["game_type_id"])

					if gametype is None:
						raise NotFound("The specified game type does not exist.")
				else:
					raise BadRequest("Argument provided for this game type is invalid.")

				GM = GameMapper()

				# Get the user by E-mail
				game = Game()

				game.setName(dataObject["name"])
				game.setCreator(self.user)
				game.setGameType(gametype)

				GM.insert(game)

				return self._response(game.dict(3), CODE.CREATED)
				
			except mdb.DatabaseError, e:
				raise ServerError("Unable to search the user database (%s)" % e.args[1])
		else:
			raise BadRequest("Required params name and game_type_id not sent")

	@require_login
	def _doPut(self, dataObject):

		# The game creation should have no arguments.
		if self.arg is None:
			raise BadRequest("An ID must be supplied in order to update a game.")

		if "name" or "game_type_id" in dataObject:
			try:
				GM = GameMapper()

				if self.arg.isdigit():
					# Get the user b ID
					game = GM.find(self.arg)
				else:
					raise BadRequest("Games must be requested by ID")

				if game is None:
					raise NotFound("There is no game identified by the number %s" % self.arg)

				# check user has the priviledges
				if not self.user.getId() == game.getCreator().getId() and not self.user.accessLevel('super_user'):
					raise Forbidden("You do not have sufficient privileges to delete this game.")

				if "game_type_id" in dataObject:

					GTM = GameTypeMapper()

					if dataObject["game_type_id"] is not None and dataObject["game_type_id"].isdigit():
						# Get the user by ID
						gametype = GTM.find(dataObject["game_type_id"])

						if gametype is None:
							raise NotFound("The specified game type does not exist.")
						else:
							game.setGameType(gametype)
					else:
						raise BadRequest("Argument provided for this game type is invalid.")

				if "name" in dataObject:
					game.setName(dataObject["name"])

				GTM.update(game)

				return self._response(game.dict(3), CODE.CREATED)
				
			except mdb.DatabaseError, e:
				raise ServerError("Unable to search the user database (%s)" % e.args[1])
		else:
			raise BadRequest("Required params name or game_type_id not sent")

	@require_login
	def _doDelete(self):
		if self.arg is None:
			raise BadRequest("You must provide the ID of the game to be deleted")
		GM = GameMapper()

		# get the user if it exists
		try:
			if self.arg.isdigit():
				# Get the user by ID
				game = GameMapper.find(self.arg)
			else:
				raise BadRequest("Games must be requested by ID")

		except mdb.DatabaseError, e:
			raise ServerError("Unable to search the user database (%s: %s)" % e.args[0], e.args[1])

		if game is None:
				raise NotFound("There is no game identified by the number %s" % self.arg)

		# check user has the priviledges
		if not self.user.getId() == game.getCreator().getId() and not self.user.accessLevel('super_user'):
			raise Forbidden("You do not have sufficient privileges to delete this game.")

		# delete the user from the data base
		result = GM.delete(game)

		if result:
			return self._response({"message": "Game Deleted Successfully."}, CODE.OK)
		else:
			raise ServerError("Unable to delete the game")