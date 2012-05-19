from Model.jsonparser import JSONParser


def postRequest (client, data):

	data = data.rstrip()
	data = data.split('\n', 1)

	try:
		parser=JSONParser()
		data_object = parser.getObject(data[1])
	
	except ValueError:
			return -1
	except IndexError:
			return -1
	
	try:
			header_http = data[0].split('\n')[0]
			data_path = header_http.split()[1]
	except IndexError:
			print "Inproper data given :%s" % data
			return -1

	## TODO: auth
	## TODO: DB call
