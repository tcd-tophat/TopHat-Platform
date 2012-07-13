#! /usr/bin/python

def main():
	from Common.config import TopHatConfig

	#setup the config
	kwargs = {"path":"/home/specialk/Dev/tophat/config.py"}
	TopHatConfig(**kwargs)

	# do the other stuff
	import Model.user
	import Model.usermetadata
	import Model.user
	import Model.kill
	import Model.usermetadata
	import Model.apitoken
	from Model.Mapper import gamemapper as GM
	from Model.Mapper import usermapper as UM
	from Model.Mapper import killmapper as KM
	from Model.Mapper import playermapper as PM
	from Model.Mapper import apitokenmapper as ATM
	from Model.Mapper import objectwatcher as OW

	# Get All the current Users from the database
	UserMapper = UM.UserMapper()
	users = UserMapper.findAll()
	for usr in users:
		print usr

	KillMapper = KM.KillMapper()
	kills = KillMapper.findAll()

	for kill_ in kills:
		print kill_

	PlayerMapper = PM.PlayerMapper()
	players = PlayerMapper.findAll()

	for player_ in players:
		print player_

	GameMapper = GM.GameMapper()
	games = GameMapper.findAll()
	for game_ in games:
		print game_

	ATM_ = ATM.ApitokenMapper()
	tokens = ATM_.findAll()
	for token in tokens:
		print token

	usr1 = UserMapper.find(1)
	#usr1.setEmail("kevin@tophat.ie")

	UserMapper.update(usr1)

	# Testing Identity Object
	#from Mapper import identityobject
	#IO = identityobject.IdentityObject(None, user.User)
	#IO.field("name").eq("Kevin Baker")

	#usersSelect = UserMapper.selectIdentity(IO, 0, 5)
	#if usersSelect:
	#	for usrS in usersSelect:
	#		print usrS

	#usr1 = UserMapper.find(1)
	#usr1.setEmail("kevin@tophat.ie")

	#OW.printAll()

	#print usr1.getEmail()

	# make all changes to DB before closing it
	#OW.magicSaveAll()

if __name__ == "__main__":
    main()