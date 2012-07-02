from urlparse import urlparse, parse_qs
import cherrypy
from Controllers.datahandler import DataHandler
from Model.jsonencoder import JsonEncoder
from Networking.statuscodes import StatusCodes

class RESTResource(object):
   """
   Base class for providing a RESTful interface to a resource.

   To use this class, simply derive a class from it and implement the methods
   you want to support.  The list of possible methods are:
   handle_GET
   handle_PUT
   handle_POST
   handle_DELETE
   """
   @cherrypy.expose
   def default(self, *vpath, **params):
      method = getattr(self, "handle_" + cherrypy.request.method, None)
      if not method:
         methods = [x.replace("handle_", "")
            for x in dir(self) if x.startswith("handle_")]
         cherrypy.response.headers["Allow"] = ",".join(methods)
         raise cherrypy.HTTPError(405, "Method not implemented.")
      return method(*vpath, **params);

class CherrypyHandler(RESTResource):

    datahandler = None

    def __init__(self, networking):
        self.networking = networking
        self.datahandler = DataHandler()

    def handle_GET(self, *vpath, **params):
        retval = "/"+str('/'.join(vpath))+"/"

        if retval == "//":
          retval = "/"

        response = self.datahandler.handleIt(0, retval, None)

        if response.code is StatusCodes.SERVER_ERROR:
          cherrypy.response.status = response.code
          return JsonEncoder.toJson({"error_code": response.code, "error_message": response.data})
        else:
          cherrypy.response.status = response.code
          return JsonEncoder.toJson(response.data)

    def handle_POST(self, *vpath, **params):
        retval = "/"+str('/'.join(vpath))+"/"

        if retval == "//":
          retval = "/"

        response = self.datahandler.handleIt(1, retval, params['data'])

        if response.code is StatusCodes.SERVER_ERROR:
          cherrypy.response.status = response.code
          return JsonEncoder.toJson({"error_code": response.code, "error_message": response.data})
        else:
          cherrypy.response.status = response.code
          return JsonEncoder.toJson(response.data)

    def handle_PUT(self, *vpath, **params):
        retval = "/"+str('/'.join(vpath))+"/"

        if retval == "//":
          retval = "/"

        response = self.datahandler.handleIt(2, retval, params['data'])

        if response.code is StatusCodes.SERVER_ERROR:
          cherrypy.response.status = response.code
          return JsonEncoder.toJson({"error_code": response.code, "error_message": response.data})
        else:
          cherrypy.response.status = response.code
          return JsonEncoder.toJson(response.data)

    def handle_DELETE(self, *vpath, **params):
        retval = "/"+str('/'.join(vpath))+"/"

        if retval == "//":
          retval = "/"

        response = self.datahandler.handleIt(3, retval, None)

        if response.code is StatusCodes.SERVER_ERROR:
          cherrypy.response.status = response.code
          return JsonEncoder.toJson({"error_code": response.code, "error_message": response.data})
        else:
          cherrypy.response.status = response.code
          return JsonEncoder.toJson(response.data)
