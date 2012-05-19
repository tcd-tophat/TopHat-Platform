import re as Regex
from Common.miscellaneous import writeTopHatToInstance

def HTTPParser(instance, data, client):

	data = data.lower()
	data = data.split('\n', 1)
	
	if data[0].find('get') is not -1:
	
		client.state.set_state('get')
	
	elif data[0].find('post') is not -1:
	
		client.state.set_state('post')
	
	elif data[0].find('delete') is not -1:
		
		client.state.set_state('delete')
	
	elif data[0].find('put') is not -1:
		
		client.state.set_state('put')
	elif data[0].find('heya') is not -1 or data[0].find('hiya') is not -1:
		client.state.set_state('undef')
		writeTopHatToInstance(instance)

	else:
		
		client.state.set_state('undef')
	return

