#!/usr/bin/env python2.7

#from twisted.internet import reactor, ssl
from os import getuid, setuid, setgid
from pwd import getpwnam
from grp import getgrnam
from sys import exit,path
from Controllers.tophatprotocol import *
from Common.miscellaneous import printTopHat
from Common.config import loadConfig
from Common.log import LogFile
from Common.date import Timestamp
from Controllers.networking import TopHatNetwork
from signal import signal, SIGINT
config=None
test=None
def Shutdown(dummy,args):
		global test
		print "[TopHat-Service shutting down]"
		test.shutdown()
		exit(0)


def TophatMain(config_path):
	global config
	config=loadConfig(config_path)
	printTopHat()
	if getuid() is not 0:
		print "The TopHat-service must be started as root to bind to port 443"
		print "[TopHat-Serivce failed to start]"
		exit(1)
	
#	factory = TopHatFactory(config) 
#	try:
#		reactor.listenSSL(config.Port, factory, ssl.DefaultOpenSSLContextFactory(config.SSLKeyPath, config.SSLCertPath), interface=config.Interface)
#	except CannotListenError as test:
		print "Cannot listen on port %s:\n%s" % (config.Port,test)
		print "[TopHat-Serivce failed to start]"
		exit(1)
	from socket import AF_INET, AF_INET6
	global test
	test = TopHatNetwork(AF_INET6, config)
	signal(SIGINT,Shutdown)

	print "Listening on port 443, deadly."


	try:
		uidNumber= getpwnam(config.User)[2] 
		print "Dropped privileges to user '%s'. Cool pops." % config.User
	except KeyError:
		print "Failed to drop privileges to user '%s'. Uh-oh." % config.User
		print "Attempting to drop to user 'nobody'"
		try:
			uidNumber= getpwnam('nobody')[2]
			print "Dropped privileges to 'nobody'. Phew!"
		except:
			print "No user 'nobody' on this system, bit mad, I'm outta here so."
			print "[TopHat-Service failed to start]"
			exit(1)
	try:
		gidNumber= getgrnam(config.User)[2] 
		print "Dropped privileges to group '%s'. Nice." % config.User
	except KeyError:
		print "Failed to drop privileges to group '%s'. :-S" % config.User
		print "Attempting to drop to group 'daemon'"
		try:
			gidNumber= getgrnam('daemon')[2]
			
			print "Dropped privileges to group 'daemon'. It seems we're in the clear, for now."
		except:
			print "No group 'nobody' on this system, I'm not going to let you run me as root. Sorry."
			print "[TopHat-Serivce failed to start]"
			exit(1)

	setgid(uidNumber)
	setuid(gidNumber)
	print "[TopHat-Service started successfully]"
	log = LogFile(config.LogFile)
	log.write("TopHat Platform (c) TopHat Software 2012\n%s: Started\n" % Timestamp())
	import asyncore
	asyncore.loop(use_poll=True)

#	reactor.run()

if __name__ == '__main__':
	TophatMain()
