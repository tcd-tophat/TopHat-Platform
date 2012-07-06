import mapper
import Model.apitoken
import usermapper as UM

class ApitokenMapper(mapper.Mapper):

	def __init__(self):
		super(ApitokenMapper, self).__init__()

	def targetClass(self):
		return "Apitoken"

	def tableName(self):
		return "api_keys"

	def _selectStmt(self):
		return "SELECT * FROM api_keys WHERE id = %s LIMIT 1"

	def _selectAllStmt(self):
		return "SELECT * FROM api_keys LIMIT %s, %s"

	def _deleteStmt(self):
		return "DELETE FROM api_keys WHERE id = %s LIMIT 1"	

	def _doCreateObject(self, data):
		"""Builds the Apitoken object using the raw data provided from the database"""
		apitoken_ = Model.apitoken.Apitoken(data["id"])

		apitoken_.setToken(data["key"])
		UserMapper = UM.UserMapper()
		apitoken_.setUser(UserMapper.find(data["user_id"]))

		return apitoken_

	def _doInsert(self, obj):
		# build query
		# id, key, group_id
		query = "INSERT INTO "+self.tableName()+" VALUES(NULL, %s, 1, %s)"

		params = (obj.getToken(), obj.getUser().getId())

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
		query = "UPDATE "+self.tableName()+" SET key = %s, user_id = %s WHERE id = %s LIMIT 1"
		params = (obj.getToken(), obj.getUser().getId(), obj.getId())

		# run the query
		cursor = self.db.getCursor()
		rowsAffected = cursor.execute(query, params)
		cursor.close()

		if rowsAffected > 0:
			return True
		else:
			return False

	def findTokenByUserId(self, user_id):
		query = "SELECT * FROM "+self.tableName()+" WHERE user_id = %s LIMIT 1"
		params = (user_id,)
	
		return self._getOne(query, params)