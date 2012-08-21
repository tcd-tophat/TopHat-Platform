from mapper import Mapp
from usermapper import UserMapper

class GameTypeMapper(Mapp):

	def __init__(self):
		super(GameTypeMapper, self).__init__()

	def targetClass(self):
		return "GameType"

	def tableName(self):
		return "game_types"

	def _selectStmt(self):
		return "SELECT * FROM game_types WHERE id = %s LIMIT 1"

	def _selectAllStmt(self):
		return "SELECT * FROM game_types LIMIT %s, %s"	

	def _deleteStmt(self, obj):
		return "DELETE FROM game_types WHERE id = %s LIMIT 1"
		
	def _doCreateObject(self, data):
		"""Builds the game object given the draw data returned from the database query"""
		from Model.gametype import GameType
		
		game_type = GameType(data["id"])
		game_type.setName(data["name"])

		return game_type

	def _doInsert(self, obj):
		# build query
		# id, name, game_type_id, creator
		query = "INSERT INTO game_types VALUES(NULL, %s)"

		# convert boolean value to int bool
		params = (obj.getName())

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
		query = "UPDATE game_types SET name = %s WHERE id = %s LIMIT 1"
		params = (obj.getName(), obj.getId())

		# run the query
		cursor = self.db.getCursor()
		rowsAffected = cursor.execute(query, params)
		cursor.close()

		if rowsAffected > 0:
			return True
		else:
			return False