class Collection(object):
	""" A non-type safe collection of raw data from the database that it will turn into objects on requet. This class is iterable """

	mapper = None
	total = 0
	raw = []

	pointer = 0
	objects = []

	def __init__(self, raw = None, mapper = None):
		self.mapper = mapper
		self.raw = raw
		self.objects = []

		if raw is not None:
			self.total = len(raw)		# set total to the number of rows of data

	def __iter__(self):
		return self

	def add(self, obj):
		""" Non-type safe method to add objects to this collection """
		# notify access for lazy load
		self._notifyAccess()

		# add to list of objects
		self.objects.append(obj)
		self.total += 1

	def __getRow(self, row):
		""" Gets a row, returning the already created object or building said object from raw data if it doesn't already exist """

		self._notifyAccess()

		# test if row is outside range
		if row < 0 or row >= self.total:
			return None

		# check if it exists in a list of already made objects
		if row > 0 and row < len(self.objects):
			return self.objects[row]

		# if not empty create and return the object made from that data
		if self.raw[row] is not None:
			self.objects.insert(row, self.mapper.createObject(self.raw[row]))
			return self.objects[row]
		else:
			return None

	def next(self):
		""" Gets the next row """
		row = self.__getRow(self.pointer) # gets the latest row

		if row is None:					
			raise StopIteration			# tells the iterator that we are done and to stop iterating
		else:
			self.pointer += 1			# increment counter
			return row

	def _notifyAccess(self):
		""" Notifies listeners of access to the data - used for lazy loading of information """
		pass			# diliberetly left blank