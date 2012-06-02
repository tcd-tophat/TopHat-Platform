from time import asctime
from networking import respondToClient
from Model.httpresponse import HttpResponse
from Model.httpdata import HttpData

def getRequest(client, response, data):
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

	try:

			http = HttpData(data, False)

			if http.getDataPath() == "/jsontest":
					response.setCode(200) # 501 = Unimplemented
					response.setData ('{"glossary": {"title": "example glossary","GlossDiv": {"title": "S","GlossList": {"GlossEntry": {"ID": "SGML","SortAs": "SGML","GlossTerm": "Standard Generalized Markup Language","Acronym": "SGML","Abbrev": "ISO 8879:1986","GlossDef": {"para": "A meta-markup language, used to create markup languages such as DocBook.","GlossSeeAlso": ["GML", "XML"]},"GlossSee": "markup"}}}}}')

			client.transport.write(response.constructResponse())
	except:
			# Respond with internal server error
			response.setCode(500)

	client.transport.write(response.constructResponse())
	client.state.set_state('done')
	return
	## TODO: auth 
   	## TODO: DB call
