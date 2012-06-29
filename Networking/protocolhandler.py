from Request.requestcontroller import RequestController

class ProtocolHandler:

	protocol = None
	protocolName = None

	def __init__(self, protocolName):
		self.protocolName = protocolName
		self.protocol = self.__importProtocol()

	def __importProtocol(self):
		title = self.protocolName.title()

		mod = self.import_item('Networking.Protocols.%s.networking' % title)

		networking = getattr(mod, "Networking")

		# load protcols networking
		loaded = networking(self)


	def networkingPush(self, opcode, uri, data):
		''' This method takes data from the network and pushes it to the data processor'''

		data = {}
		data['username'] = 'banana@tophat.ie'
		data['password'] = '123456789'

		RC = RequestController(opcode, uri, data)

		RC.run()

		if RC.response is not None:
			return "Resposne: code="+str(RC.response.code)+", data="+str(RC.response.data)
		else:
			return "REPONSE: opcode="+str(opcode)+", uri="+str(uri)+", data"+str(data)

	def import_item(self, name):
	    """Import and return bar given the string foo.bar."""

	    print name
	    package = '.'.join(name.split('.')[0:-1])
	    obj = name.split('.')[-1]

	    if package:
	        module = __import__(package,fromlist=[obj])
	        try:
	            pak = module.__dict__[obj]
	        except KeyError:
	            raise ImportError('No module named %s' % obj)
	        return pak
	    else:
	        return __import__(obj)