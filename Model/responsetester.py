#! /usr/bin/python

from httpresponse import HttpResponse


n = HttpResponse(200, "Data")

print "String HTTP: "+ str(n)

print n.constructResponse()