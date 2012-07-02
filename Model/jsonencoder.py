import json
import domainexception

# This class takes in Objects and encoes them
class JsonEncoder:

    # Get JSON as object, if not StringType, returns None.
    # Causes a ValueError to rise if invalid JSON is supplied
    @staticmethod
    def toJson(data):

    	return json.dumps(data)