from inspect import getmembers
from time import sleep
from sys import exit
class TophatClient:

	clientlist = list()
	def __init__(self, transport):
		self.port=transport.getPeer().port
		self.addr=transport.getPeer().host
		self.clientlist.append(self)
        def __str__(self):
		return "Client at %s:%d <TopHatClient>" % (self.addr,self.port)

	def __del__(self):
		clientlist.remove(self)

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

		
