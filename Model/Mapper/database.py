import MySQLdb as mdb
import sys
import gc

class Database:
	""" Class that handles the connection handler to the database """
	con = None

	def __init__(self, hostname, username, password, dbname):
		self.hostname = hostname
		self.user = username
		self.password = password
		self.dbname = dbname

		self.__connect()
	
	def __del__(self):
		self.__close()	 # on detruction of object close the connection to the DB

	def __connect(self):
		""" Makes a connection to the database"""
		gc.collect()		# runs the python garbage collector to close and possible open but unused MySQL connections
		
		try:
			self.con = mdb.connect(host=self.hostname, user=self.user, passwd=self.password, db=self.dbname, use_unicode = True, charset = "utf8")

		except mdb.Error, e:	  
			print "Database Error: %d: %s" % (e.args[0], e.args[1])
			sys.exit(1)
			
	def __close(self):
		""" Closes the connection to the database if it still exists """
		if self.con is not None:
			# close the connection
			self.con.close()

	def getCursor(self):
		""" Returns the cursor handler to the database with the setting of data being returned as an assoc array on """
		return self.con.cursor(cursorclass=mdb.cursors.DictCursor)