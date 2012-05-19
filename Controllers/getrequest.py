def getRequest(client, data):
	
	data = data.rstrip()
	data = data.split('\n') # split the header and the JSON
	try:
			header_http =  data[0].split('\n')[0]
			request_path = ( header_http.split() )[1]

	except IndexError:
			print "Inproper data given %s" % data
			return -1

	## TODO: auth 
   	## TODO: DB call
