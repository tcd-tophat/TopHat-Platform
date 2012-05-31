def deleteRequest (client, response, data):
	"""Arguments:

				client  --  Model.TophatClient
				data	--  String(Python primitive str)
		Returning:

				Integer as request_status.

				if -1 then something went wrong
				otherwise None.
		Exceptions:
				None

		Description:
				Handles DELETE requests."""
	data = data.rstrip()
	data = data.split('\n')
	try:
			header_http  = data[0].split('\n')[0]
			request_path = header_http.split()[1]

	except IndexError:
			return -1

	client.state.set_state('done')
	return
	## TODO: auth
	## TODO: DB call
