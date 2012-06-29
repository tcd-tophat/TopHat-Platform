from Model.Mapper import mapper
from Model import user

class UserMapper(mapper.Mapper):

	def __init__(self):
		super(UserMapper, self).__init__()

	def targetClass(self):
		return "User"

	def tableName(self):
		return "users"

	def _selectStmt(self):
		return "SELECT * FROM users WHERE id = %s LIMIT 1"

	def _selectAllStmt(self):
		return "SELECT * FROM users LIMIT %s, %s"

	def _deleteStmt(self, obj):
		return "DELETE FROM users WHERE id = %s LIMIT 1"	

	def _doCreateObject(self, data):
		"""Specifics required to build a User object given persistent storage data"""
		usr = user.User(data["id"])

		usr.setName(data["name"])
		usr.setPhoto(data["photo"])
		usr.setEmail(data["email"])
		usr.setPassword(data["password"])
		usr.setTime(data["time"])

		return usr

	def _doInsert(self, obj):
		# build query
		query = "INSERT INTO users VALUES(NULL, %s, %s, %s, %s, NULL)"
		params = (obj.getName(), obj.getPhoto(), obj.getEmail(), obj.getPassword())

		# run the query
		cursor = self.db.getCursor()
		rowsAffected = cursor.execute(query, params)

		# get insert id
		id_ = cursor.lastrowid
		obj.setId(id_)

		cursor.close()

		if rowsAffected > 0:
			return True
		else:
			return False

	def _doUpdate(self, obj):
		# build the query
		query = "UPDATE users SET name = %s, email = %s, photo = %s, password = %s WHERE id = %s LIMIT 1"
		params = (obj.getName(), obj.getEmail(), obj.getPhoto(), obj.getPassword(), obj.getId())

		# run the query
		cursor = self.db.getCursor()
		rowsAffected = cursor.execute(query, params)
		cursor.close()

		if rowsAffected > 0:
			return True
		else:
			return False

	def getUserByEmail(self, email):
		params = (email,)
		query = "SELECT * FROM users WHERE email = %s"
	
		return self._getOne(query, params)