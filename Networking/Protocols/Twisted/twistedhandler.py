from twisted.web.resource import Resource
from urlparse import urlparse, parse_qs
from Controllers.datahandler import DataHandler
from Model.jsonencoder import JsonEncoder
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

        if response.code >= 400:
            request.setResponseCode(response.code)
            return JsonEncoder.toJson({"error_code": response.code, "error_message": response.data})
        else:
            request.setResponseCode(response.code)
            return JsonEncoder.toJson(response.data)

    def render_POST(self, request):
        response = self.datahandler.handleIt(1, request.path, request.content.getvalue())

        if response.code >= 400:
            request.setResponseCode(response.code)
            return JsonEncoder.toJson({"error_code": response.code, "error_message": response.data})
        else:
            request.setResponseCode(response.code)
            return JsonEncoder.toJson(response.data)



    def render_PUT(self, request):
        response = self.datahandler.handleIt(2, request.path, request.content.getvalue())

        if response.code >= 400:
            request.setResponseCode(response.code)
            return JsonEncoder.toJson({"error_code": response.code, "error_message": response.data})
        else:
            request.setResponseCode(response.code)
            return JsonEncoder.toJson(response.data)

    def render_DELETE(self, request):
        response = self.datahandler.handleIt(3, request.path, None)

        if response.code >= 400:
            request.setResponseCode(response.code)
            return JsonEncoder.toJson({"error_code": response.code, "error_message": response.data})
        else:
            request.setResponseCode(response.code)
            return JsonEncoder.toJson(response.data)