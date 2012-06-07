from Model.jsonparser import JsonParser

def postRequest (client, resource, data):
	"""Arguments:

				client  	--  Model.TophatClient
				resource 	--	Model.HttpResponse
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
