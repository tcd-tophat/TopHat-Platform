#!/usr/bin/env python2.7
#from Tophat.tophat import TophatMain
from Networking.protocolhandler import ProtocolHandler
from optparse import OptionParser
from sys import exit, stderr,stdin,stdout
import sys

from os import fork, chdir, setsid, umask, dup2, getpid
from cStringIO import StringIO
if __name__ == '__main__':
		global config
		parser = OptionParser()
		parser.add_option("-c", "--config",help="Specify the location of the TopHat config file", dest='config')
		parser.add_option("-d", "--dry-run",help="Test config and quit", dest='d', default=False,action='store_true')
		parser.add_option("-f", "--foreground", help="Runs the server in the foreground instead of daemonizing", dest='f', default=False, action='store_true')
		parser.add_option("-S","--supervisor", help="Logs to stdout and does not fork so that the superviser will handle the server", dest='S', default=False, action='store_true')
		(opts, args) = parser.parse_args()
		if opts.config is None:
				print args
				print parser.print_help()
				print 'ERROR: No config file specified.'
				exit(1)
		elif opts.d:
				from Common.config import loadConfig
				loadConfig(opts.config)
				print "No syntax errors found in %s." % opts.config
				exit()
		else:
				#TophatMain(opts.config)
				from Common.config import loadConfig, TopHatConfig
				from Common.miscellaneous import printTopHat

				loadConfig(opts.config)

				

				from Common.config import TopHatConfig
				kwargs = {"path": opts.config}

				config=TopHatConfig(**kwargs).getConfig()

				p = config.Protocol(config)
				p.bind()
				if opts.f or opts.S:
					printTopHat()
					p.loop()
					
				else:
					try:
						cpid = fork()
						if cpid > 0:
							exit(0)
					except OSError, e:
						print >> stderr, 'Fork #1 failed: %d (%s)' %(e.errno, e)
						exit(1)
					chdir('/')
					setsid()
					umask(0)

					try:
						cpid = fork()
						if cpid > 0:
							si = file('/dev/null', 'r')
							so = file('/dev/null', 'a+')
							se = file('/dev/null', 'a+')
							dup2(si.fileno(), sys.stdin.fileno())
							dup2(so.fileno(), sys.stdout.fileno())
							dup2(se.fileno(), sys.stderr.fileno())
							exit(p.loop())
							pidfile = open(config.PIDFile, 'w')
							pidfile.write(getpid)
							pidfile.close()

					except OSError, e:
						print >> stderr, 'Fork #2 failed: %d (%s)' % (e.errno, e)
						exit(1)



					
