#! /usr/bin/python

import modelunittester
import user
import player
import kill
from datetime import datetime
from Mapper import database
from Mapper import usermapper as UM
from Mapper import playermapper as PM
from Mapper import killmapper as KM
from Mapper import objectwatcher as OW
from Mapper import collection

# Get All the current Users from the database
UserMapper = UM.UserMapper()
usr1 = UserMapper.find(1)
usr2 = UserMapper.find(2)
dt1 = usr1.getTime()

PlayerMapper = PM.PlayerMapper()
player1 = PlayerMapper.find(1)

KillMapper = KM.KillMapper()
kill1 = KillMapper.find(1)

data = [
	None, True, False,
	1, 0, -1, 992999, -74837294,
	0.0, 5.3, 5.8, -10.1, -14.9, 
	"0", "1", "6432", "9999999", "-999999999", 
	"hello", "hello world", 
	"invalid email@tophat.ie", "valid.email@testing.tophat.ie"
	"239738f78dc2ec1aec9d9dfb02a2325b",
	"239738f78dc2ec1aec9d9dfb02a2325b239738f78dc2ec1aec9d9dfb02a2325b239738f78dc2ec1aec9d9dfb02a2325b", 
	dt1,
	usr1,
	#player1,
	kill1
]

# setup unit tester and run it
UT = modelunittester.ModelUnitTester(player1)
UT.testFunction("name", data)
UT.testFunction("photo", data)
#UT.testFunction("game", data)
#UT.testFunction("user", data)
UT.testFunction("score", data)
#UT.testFunction("time", data)

#UT.testFunction("id", data)
#UT.testFunction("name", data)
#UT.testFunction("email", data)
#UT.testFunction("photo", data)
#UT.testFunction("time", data)"""