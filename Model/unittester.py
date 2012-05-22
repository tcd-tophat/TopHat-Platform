#! /usr/bin/python

import modelunittester
import user
from Mapper import database
from Mapper import usermapper as UM
from Mapper import objectwatcher as OW
from Mapper import collection

data = [
		True, False,
		1, 0, -1, 992999, -74837294,
		0.0, 5.3, 5.8, -10.1, -14.9, 
		"0", "1", "6432", "9999999", "-999999999", 
		"hello", "hello world", 
		"test@tophat.ie", "invalid email@tophat.ie", "valid.email@testing.tophat.ie", "valid@nyada.museum", "valid2@users.nyada.museum",
		"239738f78dc2ec1aec9d9dfb02a2325b",
		"239738f78dc2ec1aec9d9dfb02a2325b239738f78dc2ec1aec9d9dfb02a2325b239738f78dc2ec1aec9d9dfb02a2325b"]



# Get All the current Users from the database
UserMapper = UM.UserMapper()
usr = UserMapper.find(1)

# setup unit tester and run it
UT = modelunittester.ModelUnitTester(usr)
UT.testFunction("setId", "getId", data)
UT.testFunction("setName", "getName", data)
UT.testFunction("setEmail", "getEmail", data)
UT.testFunction("setPhoto", "getPhoto", data)