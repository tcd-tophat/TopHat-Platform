from Model.jsonparser import JSONParser
import urllib2

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



	data = data.rstrip()
	data = data.split('\n', 1)
	parser = JSONParser(log)
	try:
			data_object = parser.getObject(urllib2.unquote(data[1].split('=')[1]))
	except IndexError:
			return -1
	except ValueError:
			return -1
	
	try:
			header_http = data[0].split('\n')[0]
			data_path = header_http.split()[1]

			if data_path == "/api/v1/apitokens":
					response.setCode(200) # 501 = Unimplemented
					response.setData ("{\"Feature coming soon!\":\"YAY\"}")

			client.transport.write(response.constructResponse())

	except IndexError:
			return -1
	client.state.set_state('done')
	return
	## TODO: auth
	## TODO: DB call
