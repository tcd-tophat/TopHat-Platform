import mapper
import sys
import kill

class KillMapper(mapper.Mapper):

	def __init__(self):
		super(KillMapper, self).__init__()

	def targetClass(self):
		return "Kill"

	def tableName(self):
		return "kills"

	def _selectStmt(self):
		return "SELECT * FROM kills WHERE id = %s LIMIT 1"

	def _selectAllStmt(self):
		return "SELECT * FROM kills LIMIT %s, %s"	

	def _doCreateObject(self, data):
		pass

	def _doInsert(self, obj):
		print "Inserting new Kill object " + str(obj.getId())

		# build query
		# id, killer, victim, time, verified
		query = "INSERT INTO kills VALUES(NULL, %s, %s, %s, %s)"

		# convert boolean value to int bool
		if obj.getVerified():
			verfied = 1
		else:
			verfied = 0
		params = (obj.getKiller().getId(), obj.getVictim().getId(), obj.getTime(), verfied)

		# run the query
		cursor = self.db.getCursor()
		rowsAffected = cursor.execute(query, params)

		# get insert id
		id = cursor.lastrowid
		obj.setId(id)

		cursor.close()

		if rowsAffected > 0:
			return True
		else:
			return False

	def _doDelete(self, obj):
		print "Deleting Kill " + str(obj.getId())

	def _doUpdate(self, obj):
		print "Updating Kill " + str(obj.getId())

		# build the query
		query = "UPDATE kills SET killer = %s, victim = %s, time = %s, verified = %s WHERE id = %s"
		params = (obj.getKiller.getId(), obj.getVictim().getId(), obj.getPhoto(), obj.getId())

		# run the query
		cursor = self.db.getCursor()
		rowsAffected = cursor.execute(query, params)
		cursor.close()

		if rowsAffected > 0:
			return True
		else:
			return False