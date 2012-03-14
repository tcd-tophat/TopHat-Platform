import MySQLdb as mdb
import sys

class Database:
	con = None

	def __init__(self, hostname, username, password, dbname):
		self.hostname = hostname
		self.user = username
		self.password = password
		self.dbname = dbname

		self.connect()
		

	def connect(self):
		""" Makes a connection to the database"""
		try:
			self.con = mdb.connect(self.hostname, self.user, self.password, self.dbname)
			
		except mdb.Error, e:	  
			print "Database Error: %d: %s" % (e.args[0], e.args[1])
			sys.exit(1)

		finally:
			self.close()
			
	def close(self):
		if con:
			# make all changes to DB before closing it
			_ObjectWatcher.magicSaveAll()

			# close the connection
			con.close()
