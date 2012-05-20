from Model.jsonparser import JSONParser

def putRequest(client,data,log):
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
	
	data = data.rstrip()
	data = data.split('\n', 1)

	try:
		parser=JSONParser(log)
		data_object = parser.getObject(data[1]) 
	except ValueError:
		return -1
	except IndexError:
		return -1 

	header_http = data[0].split('\n')[0]
	data_path   =  header_http.split()[1]

	client.state.set_state('done')
	return



	# TODO: auth
	# TODO: DB call
