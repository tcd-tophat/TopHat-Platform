import cherrypy
from Networking.Protocols.Cherrypy.cherrypyhandler import CherrypyHandler

class Networking:

	protocol_handler = None

	def __init__(self, protocol_handler):
		self.protocol_handler = protocol_handler

		cherrypy.config.update({'server.socket_host': '127.0.0.1', 
                         'server.socket_port': 8880,
                        }) 
		cherrypy.quickstart(CherrypyHandler(self))

	def getHandler(self):
		return self.protocol_handler