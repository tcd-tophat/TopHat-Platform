from time import sleep
from sys import exit
class TophatClient:

	clientlist = list()
	def __init__(self, **kwargs):
		
		tmp = self.__client(kwargs)
		if tmp in TophatClient:

			self.port = tmp.port
			self.addr = tmp.addr
			self.state = tmp.state
			return
			
		else:
			self.port = tmp.port
			self.addr = tmp.addr
			self.state = tmp.state
			self.clientlist.append(self)
			return

	class __client:
		def __init__(self, kwargs):
			try:
				transport= kwargs['transport']
				self.port=transport.getPeer().port
				self.addr=transport.getPeer().host
				TophatClient.clientlist.append(self)
				self.state = TophatClientState()
			except KeyError:
				try:
					self.port = kwargs['port']
					self.addr = kwargs['addr']
				except KeyError:
					raise Exception("Invalid arguments passed\nCannot initialize client")
					exit(1)
		def __str__(self):
			return "Client at %s:%d <TopHatClient>" % (self.addr,self.port)
        def __str__(self):
		return "Client at %s:%d <TopHatClient>" % (self.addr,self.port)

	class __metaclass__(type):

		def __iter__(self):
			for x in TophatClient.clientlist:
				yield x
		def __len__(self):
			return len(self.clientlist)
		def __contains__(self, v):
			return v in self.clientlist
		def __getitem__(self,v):
			return self.clientlist[v]


class TophatClientState:
	__allowedstates = ['get', 'put', 'delete', 'undef','post', 'res', 'init']
	def __init__(self):
		self.set_state('init')
	
	def get_state(self):
		return self.state
	def set_state(self, new_state):
		if new_state in self.__allowedstates:
			self.state = new_state
			return
		else:
			raise Exception("Bad state %s" %new_state)
	def __str__(self):
		return "<TophatClientState>: In state %s." % self.state
	
