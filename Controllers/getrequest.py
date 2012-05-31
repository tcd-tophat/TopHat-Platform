from time import asctime
from networking import respondToClient
from Model.httpresponse import HttpResponse

def getRequest(client, data):
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
			Handles GET requests."""
	data = data.rstrip()
	data = data.split('\n') 

	try:
			header_http  = data[0].split('\n')[0]
			request_path = header_http.split()[1]

	except IndexError:
			return -1
	
	path = request_path.split('/')[1]

	if path == 'jsontest':
			response.setCode(200)
			response.setData ('{"glossary": {"title": "example glossary","GlossDiv": {"title": "S","GlossList": {"GlossEntry": {"ID": "SGML","SortAs": "SGML","GlossTerm": "Standard Generalized Markup Language","Acronym": "SGML","Abbrev": "ISO 8879:1986","GlossDef": {"para": "A meta-markup language, used to create markup languages such as DocBook.","GlossSeeAlso": ["GML", "XML"]},"GlossSee": "markup"}}}}}')
			

	client.transport.write(response.constructResponse())
	client.state.set_state('done')
	return
	## TODO: auth 
   	## TODO: DB call
