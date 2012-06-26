from Networking.protocolhandler import ProtocolHandler
import traceback, sys

p = ProtocolHandler("twisted")


t = p.getStatusCodes()

print t.OK
print StatusCodes.OK


import pprint

pprint.pprint(t)