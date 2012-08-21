from mapper import Mapp

class ApitokenMapper(Mapp):

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
		from Model.apitoken import Apitoken
		from Model.Mapper.usermapper import UserMapper

		apitoken_ = Apitoken(data["id"])

		apitoken_.setToken(data["key"])
		apitoken_.setGroup(data["group_id"])
		
		umapper = UserMapper()
		apitoken_.setUser(umapper.find(data["user_id"]))

		return apitoken_

	def _doInsert(self, obj):
		# build query
		# id, key, group_id
		query = "INSERT INTO api_keys VALUES(NULL, %s, %s, %s)"

		params = (obj.getToken(), obj.getGroup(), obj.getUser().getId())

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
		query = "UPDATE api_keys SET key = %s, user_id = %s, group_id = %s WHERE id = %s LIMIT 1"
		params = (obj.getToken(), obj.getUser().getId(), obj.getGroup(), obj.getId())

		# run the query
		cursor = self.db.getCursor()
		rowsAffected = cursor.execute(query, params)
		cursor.close()

		if rowsAffected > 0:
			return True
		else:
			return False

	def findTokenByUserId(self, user_id):
		query = "SELECT * FROM api_keys WHERE user_id = %s LIMIT 1"
		params = (user_id,)
	
		return self.getOne(query, params)

	def findByKey(self, token_id):
		query = "SELECT * FROM api_keys WHERE api_keys.key = %s LIMIT 1"
		params = (token_id,)
	
		return self.getOne(query, params)