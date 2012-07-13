#! /usr/bin/python

def main():
	from Common.config import TopHatConfig

	#setup the config
	kwargs = {"path":"/home/specialk/Dev/tophat/config.py"}
	TopHatConfig(**kwargs)

	# do the other stuff
	import Model.user
	import Model.usermetadata
	from Model.Mapper import usermapper as UM

	UserMapper = UM.UserMapper()
	usr1 = UserMapper.find(1)
	print usr1
	print usr1.getGames()
	for game in usr1.getGames():
		print game

	print usr1.dict(3)

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