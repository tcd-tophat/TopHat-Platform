from urlparse import urlparse, parse_qs
import cherrypy

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


    def __init__(self, networking):
        self.networking = networking

    def handle_GET(self, *vpath, **params):
        retval = "/"+str('/'.join(vpath))+"/"
       	
        return self.networking.getHandler().networkingPush(0, retval, '')
    def handle_POST(self, *vpath, **params):
        retval = "/"+str('/'.join(vpath))+"/"

        return self.networking.getHandler().networkingPush(1, retval, str(params))

    def handle_PUT(self, *vpath, **params):
        retval = "/"+str('/'.join(vpath))+"/"

        return self.networking.getHandler().networkingPush(2, retval, str(params))

    def handle_DELETE(self, *vpath, **params):
        retval = "/"+str('/'.join(vpath))+"/"

        return self.networking.getHandler().networkingPush(3, retval, '')