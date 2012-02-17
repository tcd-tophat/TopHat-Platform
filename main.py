from twisted.web import server, resource
from twisted.internet import reactor
from tophat.controllers.requests import Requests

#                 o  o
#      oMMMMMMMMMMMMMMMMMMMMMMoo
#      MMMMMMMMMMMMMMMMMMMMMMMMM
#      "MMMMMMMMMMMMMMMMMMMMMMMo
#      "MMMMMMMMMMMMMMMMMMMMMMMo
#      "MMMMMMMMMMMMMMMMMMMMMMMo
#      "MMMMMMMMMMMMMMMMMMMMMMM
#      "MMMMMMMMMMMMMMMMMMMMMMM"
#      oMMMMMMMMMMMMMMMMMMMMMMM
#       MMMMMMMMMMMMMMMMMMMMMMM
#       MMMMMMMMMMMMMMMMMMMMMMM
#       MMMMMMMMMMMMMMMMMMMMMMM
#       MMMMMMMMMMMMMMMMMMMMMMM
#       """"MMMMMMMMMMMMMMM"""
# ooMMoo        " " " "        oMMMoo
# oMMMMMMMo                   oMMMMMMMM
# "MMMMMMMMMMooooooooooooMoMMMMMMMMM"                                ooooo        ooooo
#   ""MMMMMMMMMMMMMMMMMMMMMMMMMMMM"                                  MMMMM       "MMMMo                         ooMo"
#       """""MMMMMMMMMMMMMM"""                                       MMMMM       "MMMMo                        MMMMM
#               oMMMMMo          o o o             o    o o          MMMMM       "MMMM"          o o o         MMMMM o           ooo o
#               oMMMMMo       oMMMMMMMMMo       MMMMMoMMMMMMMo       MMMMM       "MMMMM     ooMMMMMMMMMMo    "MMMMMMMMMM"    oMMMMMMMMMMo
#               oMMMMM"      MMMMM"""MMMMMM     oMMMMMMM"MMMMMMo     MMMMMMooooooMMMMMo     MMMMM"M"MMMMMo   ""MMMMM"""    oMMMMM"""""MM"
#               oMMMMMM     MMMMM     "MMMMo    oMMMM"     MMMMM     MMMMMMMMMMMMMMMMM"      ""      MMMMM     MMMMM       oMMMMM
#               oMMMMMo    oMMMMM      MMMMM    oMMMM      MMMMMM    MMMMM"""""""MMMMMM        ooooooMMMMo     oMMMMo      "MMMMMMoooo
#               oMMMMM"    "MMMMM      MMMMMo   oMMMMo     "MMMMo    MMMMMo      "MMMMo     oMMMMMMMMMMMMM     MMMMM        "MMMMMMMMMMMo
#               "MMMMMM    "MMMMM     oMMMMM    oMMMM      MMMMMo    MMMMM       "MMMM"    MMMMM"" " MMMMo     oMMMM           """""MMMMMM
#               "MMMMMo     MMMMM     oMMMMM    oMMMMo     MMMMM     MMMMM       "MMMMM    MMMMM     MMMM"     MMMMM                "MMMMM
#               "MMMMMo     "MMMMMooooMMMM"     oMMMMMoooMMMMMM"     MMMMM       MMMMMo    MMMMMMo oMMMMMM     oMMMMMo o   oMMooo oooMMMM"
#               MMMMMM"       "MMMMMMMMMM"      oMMMMMMMMMMMM"       MMMMMo      oMMMM"     MMMMMMMMMMMMMMM     MMMMMMMMo ""MMMMMMMMMMM""
#               oMMMMM"          " """          oMMMM """""           " "         " " "       """"""    ""        """""       """""""
#               oM""                            oMMMM
#                                               oMMMM
#                                               oMMM""
# 


reactor.listenTCP(8080, server.Site(Requests()))
reactor.run()