from Model.jsonparser import JsonParser
from Model.httpdata import HttpData
from Model.Mapper import usermapper as UM
from Model.Mapper import identityobject

def postRequest (client, response, data, log):
	"""Arguments:

				client  --  Model.TophatClient
				data	--  String(Python primitive str)
				log		--  String(Python primitive str)
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

						IO = identityobject.IdentityObject(None, user.User())
						IO.field("email").eq(http.getDataObject()['username'])
						usersSelect = UserMapper.selectIdentity(IO, 0, 1)

						try:
							user_object = usersSelect[0]

							response.setCode(200) # 501 = Unimplemented
							response.setData ("{\"Successfully retrieved user\":\"YAY\"}")

						except KeyError:
							response.setCode(404)
					else:
						response.setCode(400)


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
