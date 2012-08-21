#! /usr/bin/python

def main():
	from Networking.protocolhandler import ProtocolHandler
	from Common.config import TopHatConfig

	#setup the config
	TopHatConfig(path="/home/specialk/Dev/tophat/config.py")

	# do the other stuff
	from Model.Mapper import gamemapper as GM
	
	Mapper = GM.GameMapper()
	u = Mapper.find(1)

	from pprint import pprint
	pprint(u.dict(2))

if __name__ == "__main__":
    main()