#! /usr/bin/python

from Model.httpresponse import HttpResponse


n = HttpResponse(100, "Data")

print "String HTTP: "+ str(n)

print n.constructResponse()