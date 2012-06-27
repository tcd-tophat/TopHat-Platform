from twisted.web.resource import Resource

class TwistedHandler(Resource):

	networking = None

	isLeaf = True

	def __init__(self, networking):
		self.networking = networking
		Resource.__init__(self)

	def render_GET(self, request):
		return ("<html><body><pre>GET"+str(request.postpath)+"</pre></body></html>")

	def render_POST(self, request):
		return "<html><body><pre>POST</pre></body></html>"

	def render_PUT(self, request):
		return "<html><body><pre>PUT</pre></body></html>"

	def render_DELETE(self, request):
		return "<html><body><pre>DELETE</pre></body></html>"