from mapper import Mapp

class UserMapper(Mapp):

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
		from Model.user import User
		user_ = User(data["id"])

		user_.setName(data["name"])
		user_.setPhoto(data["photo"])
		user_.setEmail(data["email"])
		user_.setPassword(data["password"])
		user_.setTime(data["time"])

		if data["registered"] == 1:
			user_.setRegistered(True)
		else:
			user_.setRegistered(False)

		return user_

	def _doInsert(self, obj):
		if obj.getRegistered():
			registered = 1
		else:
			registered = 0

		# build query
		query = "INSERT INTO users VALUES(NULL, %s, %s, %s, %s, NULL, %s)"
		params = (obj.getName(), obj.getPhoto(), obj.getEmail(), obj.getPassword(), registered)

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
		if obj.getRegistered():
			registered = 1
		else:
			registered = 0

		# build the query
		query = "UPDATE users SET name = %s, email = %s, photo = %s, password = %s, registered = %s WHERE id = %s LIMIT 1"
		params = (obj.getName(), obj.getEmail(), obj.getPhoto(), obj.getPassword(), obj.getId(), registered)

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
	
		return self.getOne(query, params)
