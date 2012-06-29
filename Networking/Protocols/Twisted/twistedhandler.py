from twisted.web.resource import Resource
from urlparse import urlparse, parse_qs
from Request.requestcontroller import RequestController

class TwistedHandler(Resource):

	networking = None

	isLeaf = True

	def __init__(self, networking):
		self.networking = networking
		Resource.__init__(self)

	def render_GET(self, request):
		RC = RequestController(0, request.path, request.content.getvalue())

		RC.run()

		if RC.response is not None:
			return "Resposne: code="+str(RC.response.code)+", data="+str(RC.response.data)
		else:
			return "REPONSE: opcode="+str(opcode)+", uri="+str(uri)+", data"+str(data)

	def render_POST(self, request):
		RC = RequestController(1, request.path, request.content.getvalue())

		RC.run()

		if RC.response is not None:
			return "Resposne: code="+str(RC.response.code)+", data="+str(RC.response.data)
		else:
			return "REPONSE: opcode="+str(opcode)+", uri="+str(uri)+", data"+str(data)

	def render_PUT(self, request):
		RC = RequestController(2, request.path, request.content.getvalue())

		RC.run()

		if RC.response is not None:
			return "Resposne: code="+str(RC.response.code)+", data="+str(RC.response.data)
		else:
			return "REPONSE: opcode="+str(opcode)+", uri="+str(uri)+", data"+str(data)

	def render_DELETE(self, request):
		RC = RequestController(3, request.path, request.content.getvalue())

		RC.run()

		if RC.response is not None:
			return "Resposne: code="+str(RC.response.code)+", data="+str(RC.response.data)
		else:
			return "REPONSE: opcode="+str(opcode)+", uri="+str(uri)+", data"+str(data)