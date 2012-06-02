from Model.httpdata import HttpData

def putRequest(client, response, data,log):
	"""Arguments:
				
				client	--	Model.TophatClient
				data	--	String(Python primitive str) 
				log		--	String(Python primitive str)
		Returning:
				
				Integer as request_status.

				if -1 then something went wrong
				otherwise None.
		Exceptions:
				None

		Description:
				Handles PUT requests."""
	

	try:

			http = HttpData(data, True)

			if http.getDataPath() == "/api/v1/apitokens":
					response.setCode(200) # 501 = Unimplemented
					response.setData ("{\"Feature coming soon!\":\"YAY\"}")
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



	# TODO: auth
	# TODO: DB call
