
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