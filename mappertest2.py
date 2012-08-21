#! /usr/bin/python

def main():
	from Common.config import TopHatConfig

	#setup the config
	kwargs = {"path":"/home/specialk/Dev/tophat/config.py"}
	TopHatConfig(**kwargs)

	# do the other stuff
	from Model.Mapper.gamemapper import GameMapper
	from Model.Mapper.usermapper import UserMapper
	from Model.Mapper.killmapper import KillMapper
	from Model.Mapper.playermapper import PlayerMapper
	from Model.Mapper.apitokenmapper import ApitokenMapper
	from Model.Mapper.objectwatcher import ObjectWatcher

	# Get All the current Users from the database
	UM = UserMapper()
	users = UM.findAll()
	for usr in users:
		print usr

	KM = KillMapper()
	kills = KM.findAll()

	for kill_ in kills:
		print kill_

	PM = PlayerMapper()
	players = PM.findAll()

	for player_ in players:
		print player_

	GM = GameMapper()
	games = GM.findAll()
	for game_ in games:
		print game_

	ATM = ApitokenMapper()
	tokens = ATM.findAll()
	for token in tokens:
		print token

	usr1 = UM.find(1)
	#usr1.setEmail("kevin@tophat.ie")

	#UserMapper.update(usr1)

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