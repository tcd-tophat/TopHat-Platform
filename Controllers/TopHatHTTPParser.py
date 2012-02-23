from sys import path
path.append('..')
from Common.Miscellaneous import writeTopHatToInstance

def HTTPParser(instance,data):

	if data.lower().find('heya') is not -1:
		writeTopHatToInstance(instance)

		return
	return

