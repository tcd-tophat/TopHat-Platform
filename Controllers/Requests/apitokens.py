from Model.Mapper import usermapper as UM
from Model.Mapper import apitokenmapper as ATM
from Common.apikeygen import getKey
from Common.passHash import checkHash

from request import Request

class Apitokens(Request):

	def __init__(self, _response, **kwargs):
		super(Apitokens, self).__init__(_response)

	def get(self, url):
		super(Apitokens,self).get(url)
		self._response.setCode(405)			# method not allowed

	def post(self, url, dataObject):
		super(Apitokens,self).post(url, dataObject)

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
				key = ATM.findTokenByUserId(selectUser.getId())

				response.setCode(201) # created
				response.setData(self.__buildData(key))

			else:
				response.setCode(401) # not authorised

		else:
			# Anonymous login here.
			key = getKey()

			response.setCode(201) # 201 = created
			response.setData(self.__buildData(key))

	def put(self, url, dataObject):
		super(Apitokens,self).put(url, dataObject)
		self._response.setCode(405)			# method not supported

	def delete(self, url):
		super(Apitokens,self).delete(url)
		self._response.setCode(405)			# method not supported

	def __buildData(self, key):
		return "{\"apitoken\":\"" + key + "\"}"