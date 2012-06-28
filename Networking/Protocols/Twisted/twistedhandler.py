from twisted.web.resource import Resource
from urlparse import urlparse, parse_qs

class TwistedHandler(Resource):

	networking = None

	isLeaf = True

	def __init__(self, networking):
		self.networking = networking
		Resource.__init__(self)

	def render_GET(self, request):

		return self.networking.getHandler().networkingPush(0, request.path, request.content)

	def render_POST(self, request):
		try:
			return self.networking.getHandler().networkingPush(1, request.path, request.args['json'])
		except:
			request.setResponseCode(500)
			return ""

	def render_PUT(self, request):
		return self.networking.getHandler().networkingPush(2, request.path, request.content.getvalue())

	def render_DELETE(self, request):
		return self.networking.getHandler().networkingPush(3, request.path, request.content.getvalue())