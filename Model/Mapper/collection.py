class Collection(object):
	"""A non-type safe collection of raw data from the database that it will turn into objects on request. This class is iterable"""

	__mapper = None
	__total = 0
	__raw = []

	__pointer = 0
	__objects = []

	def __init__(self, raw=None, mapper=None):
		self.__mapper = mapper
		self.__raw = raw
		self.__objects = []

		if raw is not None:
			self.__total = len(raw)
		else:
			self.__total = 0

	def __iter__(self):
		"""Makes the class iterable"""
		return self

	def __contains__(self, v):
		"""Allows users to check if an item exists in the collection"""
		if v in self.__objects:
			return True
		else:
			return False

	def __getitem__(self, key):
		"""Allows users to access collection items using indices"""
		row = self.__getRow(key)

		if row is not None:
			return row
		else:
			raise IndexError

	def __setitem__(self, key):
		raise Exception("You cannot alter the contains of a collection. You may add an item to the collection using the add(obj) method.")

	def __len__(self):
		return self.__total

	def add(self, obj):
		"""Non-type safe method to add objects to this collection"""
		# notify access for lazy load
		self._notifyAccess()

		# add to list of objects
		self.__objects.append(obj)
		self.__total += 1

	def __getRow(self, row):
		"""Gets a row, returning the already created object or building said object from raw data if it doesn't already exist"""

		self._notifyAccess()

		# test if row is outside range
		if row < 0 or row >= self.__total:
			return None

		# check if it exists in a list of already made objects
		if row > 0 and row < len(self.__objects):
			return self.__objects[row]

		# if not empty create and return the object made from that data
		if self.__raw[row] is not None:
			self.__objects.insert(row, self.__mapper.createObject(self.__raw[row]))
			return self.__objects[row]
		else:
			return None

	def next(self):
		"""Gets the next row - main part of what makes this class iterable"""
		row = self.__getRow(self.__pointer) # gets the latest row

		if row is None:					
			raise StopIteration			# tells the iterator that we are done and to stop iterating
		else:
			self.__pointer += 1			# increment counter
			return row

	def _notifyAccess(self):
		"""Notifies listeners of access to the data - used for lazy loading of information"""
		pass			# diliberetly left blank

	def rewind(self):
		"""Brings the pointer back to the start of the list of objects"""
		self.__pointer = 0

	def getTotal(self):
		"""Returns the total number of objects stored in this collection"""
		return self.__total