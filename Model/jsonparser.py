from StringIO import StringIO
from json import load
import domainexception

# This class takes in JSON encoded Strings and returns them as objects
class JsonParser:

	def __init__(self, log=None):
			return

	# Get JSON as object, if not StringType, returns None.
	# Causes a ValueError to rise if invalid JSON is supplied
	@staticmethod
	def getObject(data):

		mapped = None

		try:
			assert type(data) is str

			toParse = StringIO(data)
			mapped = load(toParse)

		except AssertionError:
				raise domainexception.DomainException("The JsonParser requires a string to given for parsing")

		return mapped
