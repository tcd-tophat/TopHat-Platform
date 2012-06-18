from Model.textresponse import TextResponse


try:
	mod = __import__('Controllers.Requests.jsontestcrap', fromlist=['Jsontest'])
	klass = getattr(mod, 'Jsontest')

	obj = klass(response)
	
	obj.get("json")

	print response.constructResponse()
except ImportError:
	print "Class not found"

