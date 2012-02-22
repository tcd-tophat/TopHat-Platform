#!/usr/bin/env python2.5
from twisted.web import server, resource
from twisted.internet import reactor
from twisted.web.resource import Resource  
from twisted.web.server import Site

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


printroot = RootRequests()
root = Resource()

# Set the basic URLs we have
root.putChild("", RootRequests())
root.putChild("user", UserRequests())
root.putChild("game", GameRequests())

factory = Site(root)
reactor.listenTCP(40013, factory)
print "[TopHat-Service started successfully]"
reactor.run()


