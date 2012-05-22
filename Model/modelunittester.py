import domainexception

class ModelUnitTester:

	obj = None

	def __init__(self, obj):
		self.obj = obj

	def testFunction(self, setFunctionName, getFunctionName, data):
		print "====================================================="
		print "Testing " + setFunctionName
		for value in data:
			try:
				print "==============================="
				print "Input: " + str(value) + " " + str(type(value))	# print what value and type we are testing

				getattr(self.obj, setFunctionName)(value)			# run the set function

				result = getattr(self.obj, getFunctionName)()

				print "Output: " + str(result) + " " + str(type(result))	# get and print the value

			except domainexception.DomainException as e:
				print "*WARNING*"
				print e.message

			except Exception as e:
				print "*ERROR ERROR ERROR*"
				print type(e)
				print e