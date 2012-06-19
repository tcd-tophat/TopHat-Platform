from Model.textresponse import TextResponse

def singleRequest(client, resource, data):
	"""Arguments:

				client  	--  Model.TophatClient
				resource	--  The resource URL
				data		--  String(Python primitive str)
		Returning:

				Integer as request_status.

				if -1 then something went wrong
				otherwise None.
		Exceptions:
			None

		Description:
			Handles GET requests."""

	response = TextResponse()

	try:
		var = resource.title()

		try:
			mod = __import__('Controllers.Requests.'+var, fromlist=[var])
			klass = getattr(mod, var)

			obj = klass(response)
			
			obj.get("json")

		except:
			response.setCode(404)

print response.constructResponse()
	except:
			# Respond with internal server error
			response.setCode(500)

	client.transport.write(response.constructResponse())
	client.state.set_state('done')
	
	return
	## TODO: auth 
   	## TODO: DB call
