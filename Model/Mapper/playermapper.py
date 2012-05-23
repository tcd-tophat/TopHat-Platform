import sys

import mapper
import player
import user
import usermapper
import game
import gamemapper

class PlayerMapper(mapper.Mapper):

	def __init__(self):
		super(PlayerMapper, self).__init__()

	def targetClass(self):
		return "Player"

	def tableName(self):
		return "players"

	def _selectStmt(self):
		return "SELECT * FROM players WHERE id = %s LIMIT 1"

	def _selectAllStmt(self):
		return "SELECT * FROM players LIMIT %s, %s"	

	def _doCreateObject(self, data):
		"""Builds the kill object using the raw data provided from the database"""
		player_ = player.Player(data["id"])

		GameMapper = gamemapper.GameMapper()
		game_ = GameMapper.find(data["game_id"])
		player_.setGame(game_)

		UserMapper = usermapper.UserMapper()
		user_ = UserMapper.find(data["user_id"])
		player_.setUser(user_)

		player_.setName(data["name"])
		player_.setPhoto(data["photo"])
		player_.setLat(data["lat"])
		player_.setLon(data["lon"])
		player_.setScore(data["score"])
		player_.setTime(data["time"])

		return player_

	def _doInsert(self, obj):
		print "Inserting new Player object " + str(obj.getId())

		# build query
		# id, name, photo, game_id, user_id, lat, lon, score, time
		query = "INSERT INTO player VALUES(NULL, %s, %s, %s, %s, %s, %s, %s, %s)"

		# convert boolean value to int bool
		params = (obj.getName(), obj.getPhoto(), obj.getGame().getId(), 
				obj.getUser().getId(), obj.getLat(), obj.getLon(), obj.getScore(), obj.getTime())

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
		print "Deleting Player " + str(obj.getId())

	def _doUpdate(self, obj):
		print "Updating Player " + str(obj.getId())

		# build the query
		query = """UPDATE players SET 
					name = %s, photo = %s, game_id = %s, user_id = %s, lat = %s, lon = %s, score = %s, time = %s 
					WHERE id = %s LIMIT 1"""
		params = (obj.getName(), obj.getPhoto(), obj.getGame().getId(), 
				obj.getUser().getId(), obj.getLat(), obj.getLon(), obj.getScore(), obj.getTime(), obj.getId())

		# run the query
		cursor = self.db.getCursor()
		rowsAffected = cursor.execute(query, params)
		cursor.close()

		if rowsAffected > 0:
			return True
		else:
			return False