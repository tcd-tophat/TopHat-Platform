from Request.requestcontroller import RequestController
from Model.jsonparser import JsonParser
from Request.response import Response
from Networking.statuscodes import StatusCodes
from Model.jsonencoder import JsonEncoder
import traceback

class DataHandler:

	def __init__(self):
		pass

	def handleIt(self, opcode, uri, data):

		response = None

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
				response = RC.response
			else:
				response = Response("No data returned from requests controller.", StatusCodes.SERVER_ERROR)
		except:
			# Return Server error message with the stacktrace
			response = Response(traceback.format_exc(), StatusCodes.SERVER_ERROR)

		if response.code is StatusCodes.OK or response.code is StatusCodes.CREATED:
			response.json = JsonEncoder.toJson(response.data)
		else:
			response.json = JsonEncoder.toJson({"error_code": response.code, "error_message": response.data})

		return response