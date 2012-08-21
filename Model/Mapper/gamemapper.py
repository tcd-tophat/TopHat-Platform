import MySQLdb as mdb
from mapper import Mapp

from usermapper import UserMapper
from gametypemapper import GameTypeMapper
from deferredcollection import DeferredCollection

class GameMapper(Mapp):

	def __init__(self):
		super(GameMapper, self).__init__()

	def targetClass(self):
		return "Game"

	def tableName(self):
		return "games"

	def _selectStmt(self):
		return "SELECT g.*, t.name as game_type_name FROM games g LEFT JOIN game_types t ON g.game_type_id = t.id WHERE g.id = %s LIMIT 1"

	def _selectAllStmt(self):
		return "SELECT g.*, t.name as game_type_name FROM games g LEFT JOIN game_types t ON g.game_type_id = t.id LIMIT %s, %s"	

	def _deleteStmt(self, obj):
		return "DELETE FROM games WHERE id = %s LIMIT 1"
		
	def _doCreateObject(self, data):
		"""Builds the game object given the draw data returned from the database query"""
		from Model.game import Game
		
		game_ = Game(data["id"])

		# get creator User object
		umapper = UserMapper()
		game_.setCreator(umapper.find(data["creator"]))
		#query = "SELECT * FROM users WHERE id = %s"
		#params = (data["creator"],)
		#creator = DeferredUser(data["creator"], UserMapper, query, params)
		#game_.setCreator(creator)

		# Build the game type information
		gt_data = {}
		gt_data["id"] = data["game_type_id"]
		gt_data["name"] = data["game_type_name"]
		GTM = GameTypeMapper()
		gametype = GTM.createObject(gt_data)		# advantage is the object is added to the object watcher for future references
		print gametype
		print str(type(gametype))
		game_.setGameType(gametype)

		# set the rest of the information
		game_.setName(data["name"])
		game_.setTime(data["time"])
		game_.setStartTime(data["start_time"])
		game_.setEndTime(data["end_time"])

		return game_

	def _doInsert(self, obj):
		# build query
		# id, name, game_type_id, creator
		query = "INSERT INTO games VALUES(NULL, %s, %s, %s, NOW(), %s, %s)"

		# convert boolean value to int bool
		params = (obj.getName(), obj.getGameType().getId(), obj.getCreator().getId(), obj.getStartTime(), obj.getEndTime())

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

	def _doUpdate(self, obj):
		# build the query
		query = "UPDATE games SET name = %s, game_type_id = %s, creator = %s, start_time = %s, end_time = %s WHERE id = %s LIMIT 1"
		params = (obj.getName(), obj.getGameType().getId(), obj.getCreator().getId(), obj.getStartTime(), obj.getEndTime(), obj.getId())

		# run the query
		cursor = self.db.getCursor()
		rowsAffected = cursor.execute(query, params)
		cursor.close()

		if rowsAffected > 0:
			return True
		else:
			return False

	def findByUser(self, user, start=0, number=50):
		if start < 0:
			raise mdb.ProgrammingError("The start point must be a positive int")

		if number > 50:
			raise mdb.ProgrammingError("You cannot select more than 50 rows at one time")

		query = """SELECT g.*, gt.name as game_type_name 
					FROM games g 
					LEFT JOIN game_types gt ON g.game_type_id = gt.id 
					LEFT JOIN players p ON p.game_id = g.id 
					LEFT JOIN users u ON p.user_id = u.id 
					WHERE u.id = %s LIMIT %s, %s"""
		params = (user.getId(), start, start+number)

		return DeferredCollection(self, query, params)