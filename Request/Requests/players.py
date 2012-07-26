from Request.request import Request
from Request.requesterrors import NotFound, ServerError, Unauthorised, MethodNotAllowed, RequestError, BadRequest
from Networking.statuscodes import StatusCodes as CODE

from Model.Mapper import usermapper as UM
from Model.Mapper import gamemapper as GM
from Model.Mapper import playermapper as PM
from Model.player import Player
import MySQLdb as mdb

# Decorator
from Model.authentication import require_login, require_super_user

class Players(Request):

	''' 
		API Documentation
		Documentation for the Core Request of Games is available from the TopHat wiki at:
		http://wiki.tophat.ie/index.php?title=Core_Requests:_Players
	'''

	def __init__(self):
		super(Players, self).__init__()

	@require_super_user
	@require_login
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

	@require_login
	def _doPost(self, dataObject):

		if "name" and "game" and "photo" in dataObject:
			try:
				GameMapper = GM.GameMapper()

				if dataObject["game"] is not None and str(dataObject["game"]).isdigit():
					# Get the user by ID
					game = GameMapper.find(str(dataObject["game"]))

					if game is None:
						raise NotFound("The specified game type does not exist.")
				else:
					raise BadRequest("Argument provided for this game type is invalid.")

				print "GAME GOOD "+str(game)
				PlayerMapper = PM.PlayerMapper()

				player = Player()

				player.setName(dataObject["name"])
				player.setGame(game)
				player.setPhoto(dataObject["photo"])
				player.setUser(self.user)

				PlayerMapper.insert(player)
				print "PLAYER GOOD "+str(player)

				GameMapper.joinGame(self.user, player)

				return self._response(player.dict(3), CODE.CREATED)
				
			except mdb.DatabaseError, e:
				raise ServerError("Unable to search the user database (%s)" % e.args[1])
		else:
			raise BadRequest("Required params name, game and photo not sent")

	@require_login
	def _doPut(self, dataObject):

		if  "id" and ("name" or "photo") in dataObject:
			try:

				PlayerMapper = PM.PlayerMapper()

				if dataObject["id"] is not None and dataObject["id"].isdigit():
					# Get the user by ID
					player = PlayerMapper.find(dataObject["id"])

					if player is None:
						raise NotFound("The specified game type does not exist.")
				else:
					raise BadRequest("Argument provided for this player type is invalid.")

				if player.getUser() is self.user or self.user.accessLevel('super_user'):
					if "name" in dataObject:
						player.setName(dataObject["name"])

					if "photo" in dataObject:
						player.setPhoto(dataObject["photo"])

					PlayerMapper.update(player)

				return self._response(player.dict(3), CODE.CREATED)
				
			except mdb.DatabaseError, e:
				raise ServerError("Unable to search the user database (%s)" % e.args[1])
		else:
			raise BadRequest("Required params name, game and photo not sent")

	@require_login
	def _doDelete(self):
		if self.arg is None:
			raise MethodNotAllowed("You must provide the ID of the game to be deleted")
		
		PlayerMapper = PM.PlayerMapper()

		# get the user if it exists
		try:
			if self.arg.isdigit():
				# Get the user by ID
				player = PlayerMapper.find(self.arg)
			else:
				raise BadRequest("Games must be requested by ID")

		except mdb.DatabaseError, e:
			raise ServerError("Unable to search the user database (%s: %s)" % e.args[0], e.args[1])

		if player is None:
				raise NotFound("There is no game identified by the number %s" % self.arg)

		# check user has the priviledges
		if not self.user.getId() == player.getUser().getId() and not self.user.accessLevel('super_user'):
			raise Unauthorised("You do not have sufficient privileges to delete this game.")

		# delete the user from the data base
		result = PlayerMapper.delete(player)

		if result:
			return self._response({"message": "Game Deleted Successfully."}, CODE.OK)
		else:
			raise ServerError("Unable to delete the game")