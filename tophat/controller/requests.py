from twisted.web import server, resource
from twisted.internet import reactor

import getrequest, postrequest, deleterequest, putrequest

# Simple Counter Main method to get us started with programming.
class Requests(resource.Resource):
    numberRequests = 0

    # For some reason this line is vital - I removed it and it caused the server to crash. Strange.
    isLeaf = True

    def __init__(resource):
    	return
    
    def render_GET(self, request):
        self.numberRequests += 1
        request.setHeader("content-type", "text/plain")
        return "I am GET - request #" + str(self.numberRequests) + "\n"

    def render_POST(self, request):
        self.numberRequests += 1
        request.setHeader("content-type", "text/plain")
        return "I am POST - request #" + str(self.numberRequests) + "\n"

    def render_DELETE(self, request):
        self.numberRequests += 1
        request.setHeader("content-type", "text/plain")
        return "I am DELETE - request #" + str(self.numberRequests) + "\n"
   
    def render_PUT(self, request):
        self.numberRequests += 1
        request.setHeader("content-type", "text/plain")
        return "I am PUT - request #" + str(self.numberRequests) + "\n"