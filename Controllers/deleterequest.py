from Model.textresponse import TextResponse

def deleteRequest (client, response, data):
	"""Arguments:

				client  	--  Model.TophatClient
				resource	--  The resource URL
				data		--  String(Python primitive str)
		Returning:

				Integer as request_status.

				if -1 then something went wrong
				otherwise None.
		Exceptions:
			None

		Description:
			Handles DELETE requests."""

	response = TextResponse()

	try:
		if resource == "/jsontest":
			response.setCode(200) # 501 = Unimplemented
			response.setData ('{"glossary": {"title": "example glossary","GlossDiv": {"title": "S","GlossList": {"GlossEntry": {"ID": "SGML","SortAs": "SGML","GlossTerm": "Standard Generalized Markup Language","Acronym": "SGML","Abbrev": "ISO 8879:1986","GlossDef": {"para": "A meta-markup language, used to create markup languages such as DocBook.","GlossSeeAlso": ["GML", "XML"]},"GlossSee": "markup"}}}}}')
		elif resource == "/api/v1/users/":
			# This lists all users. Not accessible by standard access level, must be admin
			response.setCode(403)
		else:
			response.setCode(404)
	except:
			# Respond with internal server error
			response.setCode(500)

	client.transport.write(response.constructResponse())
	client.state.set_state('done')

	return
	## TODO: auth
	## TODO: DB call
