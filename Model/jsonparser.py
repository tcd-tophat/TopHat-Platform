from Common.log import LogFile
from Common.date import Timestamp  
from StringIO import StringIO
from json import load
# This class takes in JSON encoded Strings and returns them as objects
class JSONParser:

	def __init__(self, log=None):
			if log is not None:
					self.log = LogFile(log)




	# Get JSON as object, if not StringType, returns None.
	# Causes a ValueError to rise if invalid JSON is supplied
	def getObject(self, data):

		mapped = None

		try:
			assert type(data) is str

			toParse = StringIO(data)
			mapped = load(toParse)

		except AssertionError:
				if hasattr(self, 'log'):
						self.log.write("%s Invalid type into the JSON Parser. Expecting StringType" % Timestamp())

		return mapped
