class Collection(object):
	"""A non-type safe collection of raw data from the database that it will turn into objects on request. This class is iterable"""

	_mapper = None
	_total = 0
	_raw = []

	_pointer = 0
	_objects = []

	def __init__(self, raw=None, mapper=None):
		self._mapper = mapper
		self._raw = raw
		self._objects = []

		if raw is not None:
			self._total = len(raw)
		else:
			self._total = 0

	def __iter__(self):
		"""Makes the class iterable"""
		return self

	def __contains__(self, v):
		"""Allows users to check if an item exists in the collection"""
		if v in self._objects:
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
		return self._total

	def add(self, obj):
		"""Non-type safe method to add objects to this collection"""
		# notify access for lazy load
		self._notifyAccess()

		# add to list of objects
		self._objects.append(obj)
		self._total += 1

	def __getRow(self, row):
		"""Gets a row, returning the already created object or building said object from raw data if it doesn't already exist"""

		self._notifyAccess()

		# test if row is outside range
		if row < 0 or row >= self._total:
			return None

		# check if it exists in a list of already made objects
		if row > 0 and row < len(self._objects):
			return self._objects[row]

		# if not empty create and return the object made from that data
		if self._raw[row] is not None:
			self._objects.insert(row, self._mapper.createObject(self._raw[row]))
			return self._objects[row]
		else:
			return None

	def next(self):
		"""Gets the next row - main part of what makes this class iterable"""
		row = self.__getRow(self._pointer) # gets the latest row

		if row is None:
			self.rewind()					
			raise StopIteration			# tells the iterator that we are done and to stop iterating
		else:
			self._pointer += 1			# increment counter
			return row

	def _notifyAccess(self):
		"""Notifies listeners of access to the data - used for lazy loading of information"""
		pass			# diliberetly left blank

	def rewind(self):
		"""Brings the pointer back to the start of the list of objects"""
		self._pointer = 0

	def getTotal(self):
		"""Returns the total number of objects stored in this collection"""
		return self._total