from httpdata import HttpData
import pprint

#
# Set of HTTP Request Tests
# Author Kevin Bluett
#

data = 'POST /api/v1/apitokens HTTP/1.1\r\nContent-Length: 60\r\nContent-Type: application/x-www-form-urlencoded\r\nHost: www.arboroia.com\r\nConnection: Keep-Alive\r\nUser-Agent: org.tophat.android.PlatformClient 0.1a\r\n\r\njson=%7B%22password%22%3A%22%22%2C%22username%22%3A%22%22%7D'

http = None
http = HttpData(data, True)
try:
	# Test With JSON Parsing
	

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

except:
	print "TEST 1 Failed"

try:
	# Test Without JSON Parsing
	http = HttpData(data, False)

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

except:
	print "TEST 2 Failed"


data = "BAD DATA }''"

try:
	# Test With JSON Parsing
	http = HttpData(data, True)

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

except:
	print "TEST 3 Failed"


try:
	# Test Without JSON Parsing (and bad data)
	http = HttpData(data, False)

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

except:
	print "TEST 4 Failed"
