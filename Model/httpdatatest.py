from httpdata import HttpData
import pprint
import sys, traceback


def test (data, json, number):

	print " === Start Test: "+str(number)+" ==="

	try:
		# Test Without JSON Parsing
		http = HttpData(data, json)

		if (http.parseError()):
			print "Error 400 Bad Request"

		print ""
		print "Request Type:"
		pprint.pprint ( http.getRequestType() )
		print ""
		print "Status Line:"
		pprint.pprint ( http.getStatusLine() )
		print ""
		print "Data Path:"
		pprint.pprint ( http.getDataPath() )
		print ""
		print "Data Object:"
		pprint.pprint ( http.getDataObject() )
		print ""
		print "Raw Response:"
		pprint.pprint ( http.getRawResponse() )

		print ""
		print "Parse Error:"
		pprint.pprint ( http.parseError() )

	except:
		print "TEST "+str(number)+" Failed"
		traceback.print_exc(file=sys.stdout)

	print " === End Test: "+str(number)+" ==="


#
# Set of HTTP Request Tests
# Author Kevin Bluett
#

data = 'POST /api/v1/apitokens HTTP/1.1\r\nContent-Length: 60\r\nContent-Type: application/x-www-form-urlencoded\r\nHost: www.arboroia.com\r\nConnection: Keep-Alive\r\nUser-Agent: org.tophat.android.PlatformClient 0.1a\r\n\r\njson=%7B%22password%22%3A%22%22%2C%22username%22%3A%22%22%7D'

test(data, True, 1)
test(data, False, 2)

data = "BAD DATA }''"

test(data, True, 3)
test(data, False, 4)

data = "GET /jsontest HTTP/1.1\n"

test(data, True, 5)
test(data, False, 6)

data = "POST /api/v1/apitokens HTTP/1.1\\r\\nContent-Length: 60\\r\\nContent-Type: application/x-www-form-urlencoded\\r\\nHost: www.arboroia.com\\r\\nConnection: Keep-Alive\\r\\nUser-Agent: org.tophat.android.PlatformClient 0.1a\\r\\n\\r\\njson=%7B%22password%22%3A%22%22%2C%22username%22%3A%22%22%7D\n"

test(data, True, 7)
test(data, False, 8)