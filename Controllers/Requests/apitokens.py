from Model.Mapper import usermapper as UM
from Model.Mapper import apitokenmapper as ATM
from Common.apikeygen import getKey
from Common.passHash import checkHash

from request import Request

class Apitokens(Request):

	def __init__(self, response, **kwargs):
		super(Apitokens, self).__init__(response)

	def _doGet(self, url):
		self._response.setCode(405)			# method not allowed

	def _doPost(self, url, dataObject):
		response = self._response

		if dataObject.has_key('username') and dataObject.has_key('password'):

			UserMapper = UM.UserMapper()
			selectedUser = UserMapper.getUserByEmail(dataObject['username'])

			if selectedUser is None:
				# User not found in database
				response.setCode(404)
				return

			# check password is correct	return corresponding key
			if checkHash(dataObject['password'], selectedUser.getPassword()):

				ATM_ = ATM.ApitokenMapper()
				key = ATM_.findTokenByUserId(selectUser.getId())

				response.setCode(201) # created
				response.setData(self.__buildData(key))

			else:
				response.setCode(401) # not authorised

		else:
			# Anonymous login here.
			key = getKey()

			response.setCode(201) # 201 = created
			response.setData(self.__buildData(key))

	def _doPut(self, url, dataObject):
		self._response.setCode(405)			# method not supported

	def _doDelete(self, url):
		self._response.setCode(405)			# method not supported

	def __buildData(self, key):
		return '{"apitoken":"' + key + '"}'