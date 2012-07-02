from Request.requestcontroller import RequestController
from Model.jsonparser import JsonParser
from Request.response import Response
from Networking.statuscodes import StatusCodes
import traceback

class DataHandler:

	def __init__(self):
		pass

	def handleIt(self, opcode, uri, data):
		try:
			if opcode == 0:
				RC = RequestController(opcode, uri, None)
			elif opcode == 1:
				RC = RequestController(opcode, uri, JsonParser.getObject(data))
			elif opcode == 2:
				RC = RequestController(opcode, uri, JsonParser.getObject(data))
			elif opcode == 3:
				RC = RequestController(opcode, uri, None)

			RC.run()

			if RC.response is not None:
				return RC.response
			else:
				return Response("No data returned from requests controller.", StatusCodes.SERVER_ERROR)
		except:
			# Return Server error message with the stacktrace
			return Response(traceback.format_exc(), StatusCodes.SERVER_ERROR)