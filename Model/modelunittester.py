import domainexception

class ModelUnitTester:

	obj = None

	def __init__(self, obj):
		self.obj = obj

	def testFunction(self, var, data):
		setFunctionName = "set" + var.capitalize()
		getFunctionName = "get" + var.capitalize()

		good = 0
		warning = 0
		error = 0

		print "############################################################"
		print "#### Testing Attribute: " + var
		for value in data:
			try:
				print "==============="
				print "Input: " + str(value) + " " + str(type(value))	# print what value and type we are testing

				getattr(self.obj, setFunctionName)(value)			# run the set function

				result = getattr(self.obj, getFunctionName)()

				print "Output: " + str(result) + " " + str(type(result))	# get and print the value
				good += 1

			except domainexception.DomainException as e:
				print "*WARNING*: %s" % e.message
				warning += 1

			except Exception as e:
				print "*ERROR ERROR ERROR*"
				print str(type(e)) + ": " + str(e)
				error  += 1

		print "=================="
		print "Attribute: " + var
		print "Good: " + str(good)
		print "Warning: " + str(warning)
		print "Error: " + str(error)