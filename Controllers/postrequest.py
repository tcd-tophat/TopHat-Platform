from Model.jsonparser import JsonParser
from Model.httpdata import HttpData
from Model.Mapper import usermapper as UM
from Common.apikeygen import getKey

def postRequest (client, response, data, log):
	"""Arguments:

				client  	--  Model.TophatClient
				response 	--	Model.HttpResponse
				data		--  String(Python primitive str)
				log			--  String(Python primitive str)
		Returning:

				Integer as request_status.

				if -1 then something went wrong
				otherwise None.
		Exceptions:
				None

		Description:
				Handles POST requests."""

	try:

			http = HttpData(data, True)

			if http.getDataPath() == "/api/v1/apitokens":

					if http.getDataObject().has_key('username') and http.getDataObject().has_key('password'):

						UserMapper = UM()
						usersSelect = UserMapper.getUserByEmail(http.getDataObject()['username'])

						try:
							user_object = usersSelect[0]

							key = getKey()

							response.setCode(200) # 501 = Unimplemented
							response.setData ("{\"apikey\":\""+key+"\"}")

						except KeyError:
							response.setCode(404)
					else:
						key = getKey()

						response.setCode(501) # 501 = Unimplemented
						response.setData ("{\"apikey\":\""+key+"\"}")

			elif http.getDataPath() == "/api/v1/users/":
				# This method is to create a new user

			elif http.parseError():
					# Respond with error 400 - Bad Request - if an parse error occurred inside the Http input responder
					response.setCode(400)

			client.transport.write(response.constructResponse())
	except:
			# Respond with internal server error
			response.setCode(500)
			client.transport.write(response.constructResponse())
			return -1
	
	client.state.set_state('done')
	return
	## TODO: auth
	## TODO: DB call
