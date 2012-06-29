from urlparse import urlparse, parse_qs
import cherrypy
from Request.requestcontroller import RequestController
from Model.jsonparser import JsonParser

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
       	
        RC = RequestController(0, retval, None)

        RC.run()

        if RC.response is not None:
          return "Resposne: code="+str(RC.response.code)+", data="+str(RC.response.data)
        else:
          return "REPONSE: opcode="+str(0)+", uri="+str(retval)+", data"+str(params)

    def handle_POST(self, *vpath, **params):
        retval = "/"+str('/'.join(vpath))+"/"
        

        print str(params['data'])
        
        RC = RequestController(1, retval, JsonParser.getObject(str(params['data'])))

        RC.run()

        if RC.response is not None:
          return "Resposne: code="+str(RC.response.code)+", data="+str(RC.response.data)
        else:
          return "REPONSE: opcode="+str(1)+", uri="+str(retval)+", data"+str(params)

    def handle_PUT(self, *vpath, **params):
        retval = "/"+str('/'.join(vpath))+"/"
        
        RC = RequestController(2, retval, params['data'])

        RC.run()

        if RC.response is not None:
          return "Resposne: code="+str(RC.response.code)+", data="+str(RC.response.data)
        else:
          return "REPONSE: opcode="+str(2)+", uri="+str(retval)+", data"+str(params)

    def handle_DELETE(self, *vpath, **params):
        retval = "/"+str('/'.join(vpath))+"/"
        
        RC = RequestController(3, retval, None)

        RC.run()

        if RC.response is not None:
          return "Resposne: code="+str(RC.response.code)+", data="+str(RC.response.data)
        else:
          return "REPONSE: opcode="+str(3)+", uri="+str(retval)+", data"+str(params)