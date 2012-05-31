import mapper
import time

import kill
import user
import playermapper as PM

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
		"""Builds the kill object using the raw data provided from the database"""
		kill_ = kill.Kill(data["id"])

		PlayerMapper = PM.PlayerMapper()
		killer = PlayerMapper.find(data["killer_player_id"])
		victim = PlayerMapper.find(data["victim_player_id"])

		kill_.setKiller(killer)
		kill_.setVictim(victim)

		kill_.setVerified(data["verified"])
		kill_.setTime(data["time"])

		return kill_

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
		id_ = cursor.lastrowid
		obj.setId(id_)

		cursor.close()

		# only if rows were changed return a success response
		if rowsAffected > 0:
			return True
		else:
			return False

	def _doDelete(self, obj):
		print "Deleting Kill " + str(obj.getId())

	def _doUpdate(self, obj):
		print "Updating Kill " + str(obj.getId())

		# build the query
		query = "UPDATE kills SET killer = %s, victim = %s, time = %s, verified = %s WHERE id = %s LIMIT 1"
		params = (obj.getKiller.getId(), obj.getVictim().getId(), obj.getPhoto(), obj.getId())

		# run the query
		cursor = self.db.getCursor()
		rowsAffected = cursor.execute(query, params)
		cursor.close()

		if rowsAffected > 0:
			return True
		else:
			return False