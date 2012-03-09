class DomainObject:

	id = -1				# setup deafult id outside db storage range

	def __init__(self, id):
		self.id = id
