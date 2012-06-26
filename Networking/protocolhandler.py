
class ProtocolHandler:

	protocol = None

	def __init__(self, protocol):
		self.protocol = protocol


	def load(self):
		try:
			mod = __import__('Controllers.Requests.'+resource, fromlist=[var])
			klass = getattr(mod, var)

			obj = klass(response)
			
			if type 	== 0:
				obj.get(resource)
			elif type 	== 1:
				obj.post(resource, data)
			elif type	== 2:
				obj.put(resource, data)
			elif type	== 3:
				obj.delete(resource)

		except:
			response.setCode(404)

	def getStatusCodes(self):

		title = self.protocol.title()

		mod = self.import_item('Networking.protocols.%s.statuscodes' % title)

		klass = getattr(mod, "StatusCodes")

		return klass

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