class TopHatClient:
	_clients = []
	def __init__(self, **kwargs):

			try:
					self.transport = kwargs['transport']
					self.port = kwargs['transport'].getPeer().port
					self.addr = kwargs['transport'].getPeer().host
			except KeyError:
					try:
							self.port = kwargs['port']					
							self.addr = kwargs['addr']
					except KeyError:
							raise TypeError('Expected transport or port and addr kwargs got %s instead.' % str(kwargs))
			self.state = TopHatClientState()

			self._clients.append((self.port,self.addr))
	def delete(self):
			del self

	def __del__(self):
			self._clients.remove((self.port,self.addr))



	class __metaclass__(type):

		def __iter__(self):
			for x in TopHatClient._clients:
				yield x
		def __len__(self):
			return len(self._clients)
		def __contains__(self, v):
			return v in self._clients
		def __getitem__(self,v):
			return self._clients[v]
		def __del__(self):
				for x in self._clients:
						del x


class TopHatClientState:
	__allowedstates = ['get', 'put', 'delete', 'undef','post', 'res', 'init', 'done']
	def __init__(self, state=None):
			if state is None:
					self.set_state('init')
			else:
					self.set_state(state)
	
	def get_state(self):
		return self.__state
	def set_state(self, new_state):
		if new_state in self.__allowedstates:
			self.__state = new_state
			return
		else:
			raise TypeError("Bad state %s" % new_state)
	def __str__(self):
		return self.__state
	
