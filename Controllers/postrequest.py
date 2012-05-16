from twisted.web import server, resource
from twisted.internet import reactor
from Model.jsonparser import *


def postRequest (instance, data, client):

	data.split('\n', 1)
	data_object = JsonParser.getObject(data[1])
	header_http = ( data[0].split('\n') )[0]
	data_path = ( header_http.split() )[1]

	## TODO: auth
	## TODO: DB call