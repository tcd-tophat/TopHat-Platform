from twisted.web import server, resource
from twisted.internet import reactor

def deleteRequest (instance, data, client):

	data = data.rstrip()
	data = data.split('\n')
	header_http = ( data[0].split('\n') )[0]
	request_path = ( header_http.split() )[1]
	## TODO: auth
	## TODO: DB call