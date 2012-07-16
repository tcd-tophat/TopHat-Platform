import mapper
import Model.gametype
import usermapper as UM
import mappererror
import deferredcollection

class GameTypeMapper(mapper.Mapper):

	def __init__(self):
		super(GameTypeMapper, self).__init__()

	def targetClass(self):
		return "GameType"

	def tableName(self):
		return "game_types"

	def _selectStmt(self):
		return "SELECT t.* FROM "+self.tableName()+" t WHERE t.id = %s LIMIT 1"

	def _selectAllStmt(self):
		return "SELECT t.* FROM "+self.tableName()+" t WHERE t.id = %s LIMIT %s, %s"	

	def _deleteStmt(self, obj):
		return "DELETE FROM "+self.tableName()+" WHERE id = %s LIMIT 1"
		
	def _doCreateObject(self, data):
		"""Builds the game object given the draw data returned from the database query"""
		game_type_ = Model.gamettype.GameType(data["id"])

		game_type_.setName(data["name"])

		return game_type_

	def _doInsert(self, obj):
		# build query
		# id, name, game_type_id, creator
		query = "INSERT INTO "+self.tableName()+" VALUES(NULL, %s)"

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
		query = "UPDATE games SET name = %s, game_type_id = %s, creator = %s WHERE id = %s LIMIT 1"
		params = (obj.getName(), obj.getGameTypeId(), obj.getCreator().getId(), obj.getId())

		# run the query
		cursor = self.db.getCursor()
		rowsAffected = cursor.execute(query, params)
		cursor.close()

		if rowsAffected > 0:
			return True
		else:
			return False