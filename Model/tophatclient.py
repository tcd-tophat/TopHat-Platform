from time import sleep
from sys import exit
class TophatClient:
	clientlist = list()
	def __init__(self, **kwargs):
		
		self.tmp = self.__client(kwargs)
		if self.tmp in TophatClient:

			self.port = self.tmp.port
			self.addr = self.tmp.addr
			self.state = self.tmp.state
			self.transport = self.tmp.transport
			return
			
		else:
			self.port = self.tmp.port
			self.addr = self.tmp.addr
			self.state = self.tmp.state
			self.transport = self.tmp.transport
			self.clientlist.append(tmp)
			return
	def delete(self):
			del self
	def __del__(self):
			del self.tmp


	class __client:
		def __init__(self, kwargs):
			try:
				transport= kwargs['transport']
				self.port=transport.getPeer().port
				self.addr=transport.getPeer().host
				TophatClient.clientlist.append(self)
				self.state = TophatClientState()
				self.transport=transport
			except KeyError:
				try:
					self.port = kwargs['port']
					self.addr = kwargs['addr']
				except KeyError:
					raise Exception("Invalid arguments passed\nCannot initialize client")
					exit(1)
		def __str__(self):
			return "Client at %s:%d <TopHatClient>" % (self.addr,self.port)
		def __del__(self):
				TophatClient.clientlist.remove(self)
				return
		def delete(self):
				del self

	
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
	__allowedstates = ['get', 'put', 'delete', 'undef','post', 'res', 'init', 'done']
	def __init__(self, state=None):
			if state is None:
					self.set_state('init')
			else:
					self.set_state(state)
	
	def get_state(self):
		return self.state
	def set_state(self, new_state):
		if new_state in self.__allowedstates:
			self.state = new_state
			return
		else:
			raise TypeError("Bad state %s" % new_state)
	def __str__(self):
		return self.state
	
