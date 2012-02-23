from twisted.web import server, resource
from twisted.internet import reactor

# Simple Counter Main method to get us started with programming.
class GetRequest:

    def __init__(self):
    	return    
   	def getresponse(self):
   		#request.setHeader("content-type", "text/plain")
   		return "Request Get received"