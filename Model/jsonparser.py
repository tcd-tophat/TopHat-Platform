from Common.log import LogFile
from Common.date import Timestamp  
from StringIO import StringIO
import json

# This class takes in JSON encoded Strings and returns them as objects
class JSONParser(config=None):

    def __init__(self):
			if config is not None:
					self.log = LogFile(config.LogFile)




    # Get JSON as object, if not StringType, returns None.
    # Causes a ValueError to rise if invalid JSON is supplied
    def getObject(self, data):

    	mapped = None

    	try:
    		assert type(data) is str

    		toParse = StringIO(data)
    		mapped = json.load(toParse)

    	except AssertionError:
				if hasattr(self, 'log'):
						self.log.write("%s Invalid type into the JSON Parser. Expecting StringType" % Timestamp())

    	return mapped
