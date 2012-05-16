from twisted.web import server, resource
from twisted.internet import reactor
from Model.jsonparser import *

def putRequest(instance, client, data):

	data.split('\n', 1) # separate header and JSON
	data_object = JSONParser(data[1]) 
	header_http = ( data[0].split('\n') )[0]
	data_path = ( header_http.split() )[1]
	# TODO: auth
	# TODO: DB call
