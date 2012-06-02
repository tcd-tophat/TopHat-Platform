import json
import domainexception

# This class takes in Objects and encoes them
class JsonEncoder:

    def __init__(self):
    	return



    # Get JSON as object, if not StringType, returns None.
    # Causes a ValueError to rise if invalid JSON is supplied
    def toJson(self, data):

    	return json.dumps(data)