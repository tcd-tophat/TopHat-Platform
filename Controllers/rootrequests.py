from twisted.web import server, resource
from twisted.web.resource import Resource
from twisted.internet import reactor

import postrequest, deleterequest, putrequest
from userrequests import UserRequests
from getrequest import GetRequest

# Simple Counter Main method to get us started with programming.
class RootRequests(resource.Resource):
    numberRequests = 0

    # For some reason this line is vital - I removed it and it caused the server to crash. Strange.
    isLeaf = True

    # Initialise Request Processing
    def __init__(resource):
        resource.children = {}
    	return
    
    def render_GET(self, request):
        self.numberRequests += 1
        request.setHeader("content-type", "text/plain")
        request.setResponseCode(200)

        return "ROOT I AM A GET REQUEST!!!!!!! %r." % (request.prepath,)

    def render_POST(self, request):
        self.numberRequests += 1
        request.setHeader("content-type", "text/plain")
        request.setResponseCode(200)

        return "I am POST - request #" + str(self.numberRequests) + "\n"

    def render_DELETE(self, request):
        self.numberRequests += 1
        request.setHeader("content-type", "text/plain")
        request.setResponseCode(200)

        return "I am DELETE - request #" + str(self.numberRequests) + "\n"
   
    def render_PUT(self, request):
        self.numberRequests += 1
        request.setHeader("content-type", "text/plain")
        request.setResponseCode(200)

        return "I am PUT - request #" + str(self.numberRequests) + "\n"