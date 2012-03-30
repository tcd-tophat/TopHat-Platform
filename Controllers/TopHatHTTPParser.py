from sys import path
import re as Regex
path.append('..')
from Common.Miscellaneous import writeTopHatToInstance

def HTTPParser(instance,data,client):

	data = data.lower()
	if data.find('heya') is not -1 or data.find('hiya') is not -1:
		writeTopHatToInstance(instance)
	elif data.find('get') is not -1:
		client.state.set_state('get')
	elif data.find('post') is not -1:
		client.state.set_state('post')
	elif data.find('delete') is not -1:
		client.state.set_state('delete')
	elif data.find('put') is not -1:
		client.state.set_state('put')
	else:
		client.state.set_state('undef')
	return

