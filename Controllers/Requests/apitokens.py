from Model.Mapper import usermapper as UM
from Common.apikeygen import getKey

from request import Request

class JsonTest(Request):

		def __init__(self, _response, **kwargs):
				super(JsonTest, self).__init__(_response)
		
		def get(self, url):
				super(JsonTest,self).get(url)
				self._response.setCode(501)

		def post(self, url, dataObject):
				super(JsonTest,self).post(url, dataObject)

				if dataObject.has_key('username') and dataObject.has_key('password'):

					UserMapper = UM()
					usersSelect = UserMapper.getUserByEmail(dataObject['username'])

					try:
						user_object = usersSelect[0]

						key = getKey()

						response.setCode(200) # 501 = Unimplemented
						response.setData ("{\"apikey\":\""+key+"\"}")

					except KeyError:
						# User not found in database = Empty Dictionary
						response.setCode(404)
				else:
					# Anonymous login here.
					key = getKey()

					response.setCode(501) # 501 = Unimplemented
					response.setData ("{\"apikey\":\""+key+"\"}")

		def put(self, url, dataObject):
				super(JsonTest,self).put(url, dataObject)
				self._response.setCode(501)

		def delete(self, url):
				super(JsonTest,self).delete(url)
				self._response.setCode(501)