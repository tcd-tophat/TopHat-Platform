from Common.log import LogFile
from StringIO import StringIO
import json

# This class takes in JSON encoded Strings and returns them as objects
class JSONParser():

    def __init__(self):
    	self.log = LogFile()



    # Get JSON as object, if not StringType, returns None.
    # Causes a ValueError to rise if invalid JSON is supplied
    def getObject(self, data):

    	mapped = None

    	try:
    		assert type(data) is str

    		toParse = StringIO(data)
    		mapped = json.load(toParse)

    	except AssertionError:
    		self.log.write("Invalid type into the JSON Parser. Expecting StringType")

    	return mapped
