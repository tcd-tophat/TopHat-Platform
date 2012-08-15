from Request.request import Request
from Networking.statuscodes import StatusCodes as CODE

class Version(Request):

	_version = None

	def __init__(self,):
		super(Version, self).__init__()

		from Common.config import TopHatConfig

		self._version = TopHatConfig.getKey("Version")
		self._gameVersion = TopHatConfig.getKey("GameVersion")
		self._serverName = TopHatConfig.getKey("ServerTitle")

	def _doGet(self):
		rdata = {
					"platform":		"TopHat.ie Server Platform",
					"version": 		self._version,
					"game_version":	self._gameVersion,
					"server_name":	self._serverName
				}
		return self._response(rdata, CODE.OK)