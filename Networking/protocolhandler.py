
class ProtocolHandler:

	protocol = None

	def __init__(self, protocolName):
		self.protocol = self.__importProtocol(protocolName)

	def __importProtocol(self, protocolName):
		lwr = protocolName.lower()
		modulename = "Networking.Protocols.%s.%sprotocol" % (protocolName, lwr)
		classname = protocolName + "Protocol"

		try:
			# example: from Networking.Protocols.Twisted.twistedprotocol import TwistedProtocol
			module = __import__(modulename, fromlist=[classname])

			return getattr(module, classname)()

		except ImportError:
			raise ImportError("Unable to import the protocol %s" % protocolName)

	def setupNetworking(self):
		title = self.protocol.title()

		mod = self.import_item('Networking.protocols.%s.networking' % title)

		networking = getattr(mod, "Networking")

		# load protcols networking
		loaded = networking(self)


	def networkingPush(self, opcode, uri, data):
		''' This method takes data from the network and pushes it to the data processor'''

		return "REPONSE: opcode="+str(opcode)+", uri="+str(uri)+", data"+str(data)

	def import_item(self, name):
	    """Import and return bar given the string foo.bar."""
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