from twisted.web import server, resource
from twisted.internet import reactor


def getRequest(instance, data, client):

	data.split('\n') # split the header and the JSON
	header_http = ( data[0].split('\n') )[0] # get first line of header
	request_path = ( header_http.split() )[1]
	## TODO: auth 
   	## TODO: DB call