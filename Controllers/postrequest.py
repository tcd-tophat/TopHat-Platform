from Model.jsonparser import JsonParser
from Model.Mapper import usermapper as UM
from Common.apikeygen import getKey

def postRequest (client, response, data):
	"""Arguments:

				client  	--  Model.TophatClient
				response 	--	Model.HttpResponse
				data		--  String(Python primitive str)
		Returning:

				Integer as request_status.

				if -1 then something went wrong
				otherwise None.
		Exceptions:
				None

		Description:
				Handles POST requests."""

	response = TextResponse()

	try:

		# Left inside try, so that bad JSON returns a valid error code to client, rather than crashing.
		json = JsonParser()
		jsonObject = json.getObject(data)

		if resource == "/api/v1/apitokens":

			if jsonObject.has_key('username') and jsonObject.has_key('password'):

				UserMapper = UM()
				usersSelect = UserMapper.getUserByEmail(jsonObject['username'])

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

		elif resource == "/api/v1/users/":
				# This method is to create a new user
				response.setCode(501) # Unimplemented
				
		else:
				response.setCode(404)

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
