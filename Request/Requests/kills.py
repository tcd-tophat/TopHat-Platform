from Request.request import Request
from Request.requesterrors import NotFound, ServerError, BadRequest
from Networking.statuscodes import StatusCodes as CODE

from Model.Mapper.killmapper import KillMapper
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
				kills = KillMapper.findAll(offset, offset+50)

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
		return self._response({}, CODE.UNIMPLEMENTED)

	@require_login
	def _doPut(self, dataObject):
		return self._response({}, CODE.UNIMPLEMENTED)

	@require_login
	def _doDelete(self):
		return self._response({}, CODE.UNIMPLEMENTED)