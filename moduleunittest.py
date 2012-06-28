from Common.config import TopHatConfig
kwargs = {"path":"/home/specialk/Dev/tophat/config.py"}
TopHatConfig(**kwargs)

from Networking.protocolhandler import ProtocolHandler
import traceback, sys

p = ProtocolHandler("twisted")
t = p.getStatusCodes()

print t.OK

print "[DONE STATUS CODE CHECK]"

print "[LOADING NETWORKING....]"

p.setupNetworking()