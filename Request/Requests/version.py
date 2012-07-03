from Request.request import Request
from Networking.statuscodes import StatusCodes as CODE
from Request.requesterrors import NotFound, ServerError, Unauthorised, MethodNotAllowed

class Version(Request):

	_version = None

	def __init__(self,):
		super(Version, self).__init__()

		from Common.config import TopHatConfig

		self._version = TopHatConfig.getKey("Version")

	def _doGet(self):
		rdata = {}
		rdata["version"] = self._version
		return self._response(rdata, CODE.OK)