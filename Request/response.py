class Response:

	code = 0
	data = {}

	def __init__(self, data, code):
		self.code = code
		self.data = data