import collection

class DeferredCollection(collection.Collection):

	run = False
	query = ""
	params = ()

	def __init__(self, mapper, query, params):
		super(DeferredCollection, self).__init__(mapper)

		self.query = query
		self.params = params

	def _notifyAccess(self):
		# check if the query has been run before
		if not self.run:
			# run the query and build results in a collection
			cursor = self.mapper.db.getCursor()				# get the database handler
			self.total = cursor.execute(query, params)
			self.raw = cursor.fetchall()					# fetch all the data from the database
			cursor.close()

		self.run = True										# ensure we don't run the query again