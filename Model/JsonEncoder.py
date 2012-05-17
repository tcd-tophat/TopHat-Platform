from types import StringType
from twisted.web import server, resource
from twisted.internet import reactor
from Common.Log import LogFile
from StringIO import StringIO
import json

# This class takes in Objects and encoes them
class JsonEncoder(resource.Resource):

    def __init__(self):
    	self.log = LogFile()



    # Get JSON as object, if not StringType, returns None.
    # Causes a ValueError to rise if invalid JSON is supplied
    def toJson(self, data):

    	mapped = json.dumps(data)

    	return mapped