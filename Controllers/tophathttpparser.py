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

	elif Regex.compile("^hiya|^heya").match(data[0]):
		client.state.set_state('undef')
		writeTopHatToInstance(instance)

	else:
		client.state.set_state('undef')
	
	return

