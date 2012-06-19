from Model.textresponse import TextResponse
import traceback, sys

response = TextResponse()

resource = "jsontest"

try:
	var = resource.title()

	try:
		mod = __import__('Controllers.Requests.'+resource, fromlist=[var])
		klass = getattr(mod, var)

		obj = klass(response)
		
		obj.get("json")

	except:
		response.setCode(404)
		traceback.print_exc(file=sys.stdout)
except:
		# Respond with internal server error
		response.setCode(500)
		traceback.print_exc(file=sys.stdout)

print response.constructResponse()