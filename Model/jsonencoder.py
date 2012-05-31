from Common.log import LogFile
import json

# This class takes in Objects and encoes them
class JsonEncoder:

    def __init__(self):
    	self.log = LogFile()



    # Get JSON as object, if not StringType, returns None.
    # Causes a ValueError to rise if invalid JSON is supplied
    def toJson(self, data):

    	mapped = json.dumps(data)

    	return mapped