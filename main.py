from twisted.web import server, resource
from twisted.internet import reactor


# Simple Counter Main method to get us started with programming.
class Main(resource.Resource):
    isLeaf = True 
    numberRequests = 0
    
    def render_GET(self, request):
        self.numberRequests += 1
        request.setHeader("content-type", "text/plain")
        return "I am request #" + str(self.numberRequests) + "\n"

reactor.listenTCP(8080, server.Site(Main()))
reactor.run()