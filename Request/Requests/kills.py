from Request.request import Request
from Request.requesterrors import NotFound, ServerError, BadRequest
from Networking.statuscodes import StatusCodes as CODE

from Model.kill import Kill
from Model.Mapper.killmapper import KillMapper
from Model.Mapper.gamemapper import GameMapper
from Model.Mapper.playermapper import PlayerMapper
from Common.utils import parseDateTime
import MySQLdb as mdb

# Decorator
from Model.authentication import require_login

class Kills(Request):

	''' 
		API Documentation
		Documentation for the Core Request of Games is available from the TopHat wiki at:
		http://wiki.tophat.ie/index.php?title=Core_Requests:_Kills
	'''

	def __init__(self):
		super(Kills, self).__init__()

	@require_login
	def _doGet(self):
		try:
			
			KM = KillMapper()
			
			if self.arg is not None:
				if self.arg.isdigit():
					# Get the user by ID
					kill = KM.find(self.arg)
				else:
					raise BadRequest("Kill must be requested by ID")

				if kill is not None:
					return self._response(kill.dict(), CODE.OK)
				else:
					raise NotFound("This kill does not exist")
			
			else:

				offset = 0
				kills = KM.findAll(offset, offset+50)

				killslist = []

				for kill in kills:
					killslist.append(kill.dict())

				killdict = {"kills":killslist, "pagination_offset":offset, "max_perpage": 50}

				return self._response(killdict, CODE.OK)

		except mdb.DatabaseError, e:
				raise ServerError("Unable to search the kill database (%s: %s)" % e.args[0], e.args[1])

		return self._response({}, CODE.UNIMPLEMENTED)

	@require_login
	def _doPost(self, dataObject):

		if "killer" and "victim" and "time" in dataObject:
			try:
				KM = KillMapper()
				GM = GameMapper()
				PM = PlayerMapper()

				if dataObject["killer"] is not None and dataObject["victim"] is not None:

					if "id" in dataObject["killer"] and "id" in dataObject["victim"]:
						# Get the user by ID
						killer = PM.find(dataObject["killer"]["id"])

						victim = PM.find(dataObject["victim"]["id"])

						try:
							proptime = parseDateTime(dataObject["time"])
						except:
							raise BadRequest("""Invalid Time object sent, acceptable formats: 	Acceptable formats are: "YYYY-MM-DD HH:MM:SS.ssssss+HH:MM",
							"YYYY-MM-DD HH:MM:SS.ssssss",
							"YYYY-MM-DD HH:MM:SS+HH:MM",
							"YYYY-MM-DD HH:MM:SS" """)

						if killer is None or victim is None:
							raise NotFound("Either the victim or the killer were invalid player objects")
					else:
						raise BadRequest("Arguments provided for this kill are invalid.")

				else:
					raise BadRequest("Arguments provided for this kill are invalid.")

				kill = Kill()

				kill.setKiller(killer)
				kill.setVictim(victim)
				kill.setVerified(False)

				kill.setTime(proptime)

				KM.insert(kill)

				return self._response(kill.dict(3), CODE.CREATED)
				
			except mdb.DatabaseError, e:
				raise ServerError("Unable to search the user database (%s)" % e.args[1])
		else:
			raise BadRequest("Killer, victim and time were not submitted")

	@require_login
	def _doPut(self, dataObject):
		return self._response({}, CODE.UNIMPLEMENTED)

	@require_login
	def _doDelete(self):
		return self._response({}, CODE.UNIMPLEMENTED)