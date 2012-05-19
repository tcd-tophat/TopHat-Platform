from twisted.internet import reactor
from Model.jsonparser import JSONParser

def putRequest(client,data):

	from sys import exit

	print data.split('\n')[0]
	data = data.rstrip()
	data = data.split('\n', 1) # separate header and JSON

	try:
		parser=JSONParser()
		data_object = parser.getObject(data[1]) 
	except ValueError:
		return -1 

	header_http = data[0].split('\n')[0]
	data_path   =  header_http.split()[1]
	# TODO: auth
	# TODO: DB call
