from twisted.web.resource import Resource
from urlparse import urlparse, parse_qs
from Controllers.datahandler import DataHandler
from Networking.statuscodes import StatusCodes

class TwistedHandler(Resource):

    networking = None

    isLeaf = True

    def __init__(self, networking):
        self.networking = networking
        self.datahandler = DataHandler()
        Resource.__init__(self)

    def render_GET(self, request):
        response = self.datahandler.handleIt(0, request.path, None)

        request.setResponseCode(response.code)
        return response.json

    def render_POST(self, request):
        response = self.datahandler.handleIt(1, request.path, request.content.getvalue())

        request.setResponseCode(response.code)
        return response.json

    def render_PUT(self, request):
        response = self.datahandler.handleIt(2, request.path, request.content.getvalue())

        request.setResponseCode(response.code)
        return response.json

    def render_DELETE(self, request):
        response = self.datahandler.handleIt(3, request.path, None)

        request.setResponseCode(response.code)
        return response.json