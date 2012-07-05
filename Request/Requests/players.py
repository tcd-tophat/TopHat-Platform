from request import Request
from requesterrors import NotFound, ServerError, Unauthorised, MethodNotAllowed
from Networking.statuscodes import StatusCodes as CODE

# Decorator
from Model.authentication import requireapitoken

class Players(Request):

	''' 
		API Documentation
		Documentation for the Core Request of Games is available from the TopHat wiki at:
		http://wiki.tophat.ie/index.php?title=Core_Requests:_Players
	'''

	def __init__(self):
		super(Players, self).__init__()

	@requireapitoken
	def _doGet(self):
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