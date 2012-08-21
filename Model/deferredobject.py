class DeferredObject:

	_run = False
	_query = ""
	_params = ()
	_mapper = None

	def __init__(self, query, params):
		self._query = query
		self._params = params

	def notifyAccess(self):
		"""The deffered work code block"""
		# check if the query has been run before
		if not self._run:
			raw = self._mapper.getOneRaw(self._query, self._params)

			self.setName(data["name"])
			self.setPhoto(data["photo"])
			self.setEmail(data["email"])
			self.setPassword(data["password"])
			self.setTime(data["time"])

			self._run = True										# ensure we don't run the query again