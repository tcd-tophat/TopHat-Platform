

class DefferedObject:

	_run = False
	_query = ""
	_params = ()
	_mapper = None

	_object = None

	def __init__(self, mapper, query, params):
		self._mapper = mapper
		self._query = query
		self._params = params

	def _run(self):
		# check if the query has been run before
		if not self._run:
			self._object = self._mapper.getOne(self._query, self._params)

		self._run = True										# ensure we don't run the query again