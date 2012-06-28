from Request.request import Request
from Model.authentication import requirelogin
from Networking.statuscodes import StatusCodes as CODE
from Request.requesterrors import NotFound, ServerError, Unauthorised, MethodNotAllowed

class Jsontest(Request):

	def __init__(self,):
		super(Jsontest, self).__init__()

	@requirelogin
	def _doGet(self):
		# Anonymous login
		rdata = {}
		rdata["crap"] = "datiubsfvius"
		return self._response(rdata, CODE.OK)