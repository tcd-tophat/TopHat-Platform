from sys import path
import re as Regex
path.append('..')
from Common.Miscellaneous import writeTopHatToInstance

def HTTPParser(instance,data):

	if data.lower().find('heya') is not -1 or data.lower().find('hiya') is not -1:
		writeTopHatToInstance(instance)

		return
	return

