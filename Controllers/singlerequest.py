from Model.textresponse import TextResponse

def quickRequest(client, type, resource, data):
	"""Arguments:

				client  	--  Model.TophatClient
				type		-- The state variable about the type this is
				resource	--  The resource URL
				data		--  String(Python primitive str)
		Returning:

				Integer as request_status.

				if -1 then something went wrong
				otherwise None.
		Exceptions:
			None

		Description:
			Handles ALL requests."""

	response = TextResponse()

	try:
		# Capitalize first letter for the class name
		var = resource.title()

		try:
			mod = __import__('Controllers.Requests.'+resource, fromlist=[var])
			klass = getattr(mod, var)

			obj = klass(response)
			
			if type 	== 0:
				obj.get(resource)
			elif type 	== 1:
				obj.post(resource, data)
			elif type	== 2:
				obj.put(resource, data)
			elif type	== 3:
				obj.delete(resource)

		except:
			response.setCode(404)
	except:
			# Respond with internal server error
			response.setCode(500)
	
	return response
	## TODO: auth 
   	## TODO: DB call
