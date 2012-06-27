from Networking.protocolhandler import ProtocolHandler
import traceback, sys

p = ProtocolHandler("twisted")
t = p.getStatusCodes()

print t.OK

print "[DONE STATUS CODE CHECK]"

print "[LOADING NETWORKING....]"

p.setupNetworking()