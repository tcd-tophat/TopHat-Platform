class Field(object):
	name = None
	operator = None
	comps = []
	incomplete = False

	def __init__(self, name):
		self.comps = []
		self.name = name

	def addTest(self, operator, value):
		self.comps.append( {'name':self.name, 'operator':operator, 'value':value} )

	def isIncomplete(self):
		if not self.comps:
			return True
		else:
			return False