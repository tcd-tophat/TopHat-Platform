import traceback

from Request.requestcontroller import RequestController
from Model.jsonparser import JsonParser
from Request.response import Response
from Networking.statuscodes import StatusCodes
from Model.jsonencoder import JsonEncoder
from Request.requesterrors import RequestError

class DataHandler:

	def __init__(self):
		pass

	def handleIt(self, opcode, uri, key, data):

		response = None

		try:
			if opcode == 0:
				RC = RequestController(opcode, uri, key, None)
			elif opcode == 1:
				RC = RequestController(opcode, uri, key, JsonParser.getObject(data))
			elif opcode == 2:
				RC = RequestController(opcode, uri, key, JsonParser.getObject(data))
			elif opcode == 3:
				RC = RequestController(opcode, uri, key, None)

			RC.run()

			if RC.response is not None:
				response = RC.response
			else:
				response = Response("No data returned from requests controller.", StatusCodes.SERVER_ERROR)
		except RequestError as e:
			# Handles Errors raised in requests. Errors contain a message and errorcode.
			response = Response(e.message, e.code)
		except ValueError:
			response = Response("JSON Data was invalid.", StatusCodes.BAD_REQUEST)
		except:
			# Return Server error message with the stacktrace
			response = Response(traceback.format_exc(), StatusCodes.SERVER_ERROR)

		if response.code is StatusCodes.OK or response.code is StatusCodes.CREATED:
			response.json = JsonEncoder.toJson(response.data)
		else:
			response.json = JsonEncoder.toJson({"error_code": response.code, "error_message": response.data})

		return response