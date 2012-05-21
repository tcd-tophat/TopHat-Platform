import re as Regex
from Common.miscellaneous import writeTopHatToInstance

def HTTPParser(instance, data, client):

	
	

	data = data.lower()
	data = data.split('\n', 1)
	
	if Regex.compile("^get").match(data[0]):
			client.state.set_state('get')
	
	elif Regex.compile("^post").match(data[0]):	
		client.state.set_state('post')
	
	elif Regex.compile("^delete").match(data[0]):		
		client.state.set_state('delete')

	elif Regex.compile("^put").match(data[0]):		
		client.state.set_state('put')

	elif Regex.compile("^jsontest").match(data[0]):
		json='{"glossary": {"title": "example glossary","GlossDiv": {"title": "S","GlossList": {"GlossEntry": {"ID": "SGML","SortAs": "SGML","GlossTerm": "Standard Generalized Markup Language","Acronym": "SGML","Abbrev": "ISO 8879:1986","GlossDef": {"para": "A meta-markup language, used to create markup languages such as DocBook.","GlossSeeAlso": ["GML", "XML"]},"GlossSee": "markup"}}}}}'
		client.state.set_state('undef')
		instance.transport.write(json)
		instance.transport.loseConnection()
	
	elif Regex.compile("^hiya|^heya").match(data[0]):
		client.state.set_state('undef')
		writeTopHatToInstance(instance)

	else:
		client.state.set_state('undef')
	
	return

