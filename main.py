#!/usr/bin/env python2.6
from twisted.web import server, resource
from twisted.internet import reactor
from twisted.web.resource import Resource  
from twisted.web.server import Site
from os import getuid, setuid, setgid
from pwd import getpwnam
from grp import getgrnam
from sys import exit
#Import the controllers.
from tophat.controller.rootrequests import RootRequests
from tophat.controller.userrequests import UserRequests
from tophat.controller.gamerequests import GameRequests

print "                 o  o          "
print "      oMMMMMMMMMMMMMMMMMMMMMMoo"
print "      MMMMMMMMMMMMMMMMMMMMMMMMM"
print "      \"MMMMMMMMMMMMMMMMMMMMMMMo"
print "      \"MMMMMMMMMMMMMMMMMMMMMMMo"
print "      \"MMMMMMMMMMMMMMMMMMMMMMMo"
print "      \"MMMMMMMMMMMMMMMMMMMMMMM"
print "      \"MMMMMMMMMMMMMMMMMMMMMMM\""
print "      oMMMMMMMMMMMMMMMMMMMMMMM"
print "       MMMMMMMMMMMMMMMMMMMMMMM"
print "       MMMMMMMMMMMMMMMMMMMMMMM"
print "       MMMMMMMMMMMMMMMMMMMMMMM"
print "       MMMMMMMMMMMMMMMMMMMMMMM"
print "      \"\"\"\"MMMMMMMMMMMMMMM\"\"\""
print "ooMMoo        \" \" \" \"        oMMMoo"
print "oMMMMMMMo                   oMMMMMMMM"
print "\"MMMMMMMMMMooooooooooooMoMMMMMMMMM\"                                ooooo        ooooo"
print "  \"\"MMMMMMMMMMMMMMMMMMMMMMMMMMMM\"                                  MMMMM       \"MMMMo                         ooMo\""
print "      \"\"\"\"\"MMMMMMMMMMMMMM\"\"\"                                       MMMMM       \"MMMMo                        MMMMM"
print "              oMMMMMo          o o o             o    o o          MMMMM       \"MMMM\"          o o o         MMMMM o           ooo o"
print "              oMMMMMo       oMMMMMMMMMo       MMMMMoMMMMMMMo       MMMMM       \"MMMMM     ooMMMMMMMMMMo    \"MMMMMMMMMM\"    oMMMMMMMMMMo"
print "              oMMMMM\"      MMMMM\"\"\"MMMMMM     oMMMMMMM\"MMMMMMo     MMMMMMooooooMMMMMo     MMMMM\"M\"MMMMMo   \"\"MMMMM\"\"\"    oMMMMM\"\"\"\"\"MM\""
print "              oMMMMMM     MMMMM     \"MMMMo    oMMMM\"     MMMMM     MMMMMMMMMMMMMMMMM\"      \"\"      MMMMM     MMMMM       oMMMMM"
print "              oMMMMMo    oMMMMM      MMMMM    oMMMM      MMMMMM    MMMMM\"\"\"\"\"\"\"MMMMMM        ooooooMMMMo     oMMMMo      \"MMMMMMoooo"
print "              oMMMMM\"    \"MMMMM      MMMMMo   oMMMMo     \"MMMMo    MMMMMo      \"MMMMo     oMMMMMMMMMMMMM     MMMMM        \"MMMMMMMMMMMo"
print "              \"MMMMMM    \"MMMMM     oMMMMM    oMMMM      MMMMMo    MMMMM       \"MMMM\"    MMMMM\"\" \" MMMMo     oMMMM           \"\"\"\"\"MMMMMM"
print "              \"MMMMMo     MMMMM     oMMMMM    oMMMMo     MMMMM     MMMMM       \"MMMMM    MMMMM     MMMM\"     MMMMM                \"MMMMM"
print "              \"MMMMMo     \"MMMMMooooMMMM\"     oMMMMMoooMMMMMM\"     MMMMM       MMMMMo    MMMMMMo oMMMMMM     oMMMMMo o   oMMooo oooMMMM\""
print "              MMMMMM\"       \"MMMMMMMMMM\"      oMMMMMMMMMMMM\"       MMMMMo      oMMMM\"     MMMMMMMMMMMMMMM     MMMMMMMMo \"\"MMMMMMMMMMM\"\""
print "              oMMMMM\"          \" \"\"\"          oMMMM \"\"\"\"\"           \" \"         \" \" \"       \"\"\"\"\"\"    \"\"        \"\"\"\"\"       \"\"\"\"\"\"\""
print "              oM\"\"                            oMMMM"
print "                                              oMMMM"
print "                                              oMMM"""

if getuid() is not 0:
	print "The TopHat-service must be started as root to bind to port 443"
	print "[TopHat-Serivce failed to start]"
	from sys import exit
	exit(1)

printroot = RootRequests()
root = Resource()

# Set the basic URLs we have
root.putChild("", RootRequests())
root.putChild("user", UserRequests())
root.putChild("game", GameRequests())

factory = Site(root)
reactor.listenTCP(443, factory)





uidNumber= getpwnam('tophat')[2]
gidNumber= getgrnam('tophat')[2]
try:
	setgid(uidNumber)
except OSError:
	print "Failed to drop privileges to group tophat"
	print "Attempting to drop to group \"nobody\""
	try:
		setgid(getgrnam('nobody')[2])
	except OSError:
		print "Unable to drop to group \"nobody\", bailing out from crazy town."
		print "[TopHat-Serivce failed to start]"
		exit(1)

try:
	setuid(gidNumber)
except OSError:
	print "Failed to drop privileges to user tophat"
	print "Attempting to drop to user \"nobody\""
	try:
		setuid(getpwnam('nobody')[2])
	except OSError:
		print "Unable to drop to user \"nobody\", this system is a mess, bailing out."
		print "[TopHat-Serivce failed to start]"
		exit(1)
print "[TopHat-Service started successfully]"
reactor.run()


