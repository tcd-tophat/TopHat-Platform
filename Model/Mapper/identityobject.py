from field import Field

class IdentityObject:

	currentField = None
	fields = {}
	__and = None
	__enforce = []

	def __init__(self, field=None, obj=None):
		if obj is not None:
			self.__enforce = self._getAttributesFromObject(obj)		# list of the object properties

		if field is not None:
			self.field(field)

	def _getAttributesFromObject(self, obj):
		"""Builds a list of allowed variables based on the attributes in the domain object"""
		attr_list = []

		for attr in dir(obj):						# foreach class attribute
			if not callable(getattr(obj, attr)):	# check not a function
				if (
					"__" not in attr and 			# except python
					"_abc_" not in attr and 		# except abstract base class
					attr is not "_data"				# except the data container
					):
					attr_list.append(attr[1:])		# remove starting _ and add to

		return attr_list

	def isVoid(self):
		"""Checks that this does have some fields set already"""
		if not self.fields:
			return True
		else:
			return False

	def field(self, name):
		"""Changes the current field to the given parameter field"""
		# check field is not incomplete
		if not self.isVoid() and self.currentField.isIncomplete():
			raise Exception("Incomplete field")

		# check we have a legal field name
		self.enforeField(name)

		# check if the field has already been created 
		if name in self.fields:
			self.currentField = self.fields[name]

		else:
			self.currentField = Field(name)			# create new field
			self.fields[name] = self.currentField			# add new field to dict of fields using key as

		return self

	def enforeField(self, name):
		"""Checks if a given field name is on the enforce whitelist, if any such list exists"""
		if self.__enforce:																				# check any such list not empty
			if name not in self.__enforce:																# check if fieldname is on the 
				enforceString = ', '.join(self.__enforce)												# implode the key names together
				raise Exception("Field " + name + " is not a valid fieldname (" + enforceString + ")")

	def __operator(self, symbol, value):
		if self.isVoid():
			raise Exception("No object field defined")

		self.currentField.addTest(symbol, value)

		return self

	def eq(self, value):
		"""Equals operator"""
		return self.__operator("=", value)

	def lt(self, value):
		"""Less than operator"""
		return self.__operator("<", value)

	def gt(self, value):
		"""Greater than operator"""
		return self.__operator(">", value)

	def like(self, value):
		"""Uses MySQL LIKE operator"""
		return self.__operator("LIKE", value)