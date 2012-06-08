import MySQLdb as mdb
import sys
import gc

class Database:
	"""Class that handles the connection handler to the database"""
	__con = None

	def __init__(self, hostname, username, password, dbname):
		self.__hostname = hostname
		self.__user = username
		self.__password = password
		self.__dbname = dbname

		self.__connect()
	
	def __del__(self):
		self.__close()	 # on detruction of object close the connection to the DB

	def __connect(self):
		"""Makes a connection to the database"""
		gc.collect()		# runs the python garbage collector to close and possible open but unused MySQL connections
		
		try:
			self.__con = mdb.connect(host=self.__hostname, user=self.__user, passwd=self.__password, db=self.__dbname, use_unicode=True, charset="utf8")

		except mdb.Error, e:
			print "Database Error: %d: %s" % (e.args[0], e.args[1])
			sys.exit(1)
			
	def __close(self):
		"""Closes the connection to the database if it still exists"""
		if self.__con is not None:
			# close the connection
			self.__con.close()

	def getCursor(self):
		"""Returns the cursor handler to the database with the setting of data being returned as an assocative array on"""
		return self.__con.cursor(cursorclass=mdb.cursors.DictCursor)