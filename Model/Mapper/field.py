class Field(object):
	name = None
	operator = None
	comps = []
	incomplete = False

	def __init__(self, name):
		self.comps = []
		self.name = name

	def addTest(self, operator, value):
		"""Adds a comparison test using the given operator and value against this instance of the filed object"""
		self.comps.append({'name':self.name, 'operator':operator, 'value':value})

	def isIncomplete(self):
		"""Test that some components to the test exist"""
		if not self.comps:
			return True
		else:
			return False