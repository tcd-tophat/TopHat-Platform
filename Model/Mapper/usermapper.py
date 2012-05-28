import mapper
import user

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

	def _doCreateObject(self, data):
		"""Specifics required to build a User object given persistent storage data"""
		usr = user.User(data["id"])

		usr.setName(data["name"])
		usr.setPhoto(data["photo"])
		usr.setEmail(data["email"])
		usr.setPassword(data["password"])

		return usr

	def _doInsert(self, obj):
		print "Inserting new User object " + str(obj.getId())

		# build query
		query = "INSERT INTO users VALUES(NULL, %s, %s, %s, %s)"
		params = (obj.getName(), obj.getPhoto(), obj.getEmail(), obj.getPassword())

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
		print "Deleting User " + str(obj.getId())

	def _doUpdate(self, obj):
		print "Updating User " + str(obj.getId())

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