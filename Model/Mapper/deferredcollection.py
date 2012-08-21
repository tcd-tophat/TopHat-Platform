from collection import Collection

class DeferredCollection(Collection):

	_run = False
	_query = ""
	_params = ()

	def __init__(self, mapper, query, params):
		super(DeferredCollection, self).__init__(None, mapper)

		self._query = query
		self._params = params

	def _notifyAccess(self):
		# check if the query has been run before
		if not self._run:
			# run the query and build results in a collection
			cursor = self._mapper.db.getCursor()				# get the database handler
			self._total = cursor.execute(self._query, self._params)
			self._raw = cursor.fetchall()					# fetch all the data from the database
			cursor.close()

		self._run = True										# ensure we don't run the query again