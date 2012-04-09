import collection

class DeferredCollection(Collection):

	run = False
	query = ""
	params = ()

	def __init__(self, mapper, query, params):
		super(DeferredCollection, self).__init__(mapper)

		self.query = query
		self.params = params

	def _notifyAccess(self):
		# check if the query has been run before
		if self.run == False:
			# run the query and build results in a collection
			cursor = self.mapper.db.getCursor()				# get the database handler
			self.total = cursor.execute(query, params)		# run the query
			self.raw = cursor.fetchall()					# fetch all the data from the database
			cursor.close()									# close out that cursor

		self.run = True										# make sure we don't run the query again