import mapper
import sys
import User

class UserMapper(mapper.Mapper):

	def __init__(self):
		super(UserMapper, self).__init__()

	def targetClass(self):
		return "User"

	def _selectStmt(self):
		return "SELECT * FROM users WHERE id = %s LIMIT 1"

	def _selectAllStmt(self):
		return "SELECT * FROM users LIMIT %s, %s"	

	def _doCreateObject(self, data):
		user = User.User(data["id"])

		user.name = data["name"]
		user.photo = data["photo"]
		user.email = data["email"]

		return user

	def _doInsert(self, obj):
		print "Inserting new User object " + str(obj.id)

		# build query
		query = "INSERT INTO users VALUES(NULL, %s, %s, %s)"
		params = (obj.name, obj.photo, obj.email)

		# run the query
		cursor = self.db.getCursor()
		rowsAffected = cursor.execute(query, params)
		cursor.close()

		if rowsAffected > 0:
			return True
		else:
			return False

	def _doDelete(self, obj):
		print "Deleting User " + str(obj.id)

	def _doUpdate(self, obj):
		print "Updating User " + str(obj.id)

		# build the query
		query = "UPDATE users SET id = %s, name = %s, email = %s, photo = %s WHERE id = %s"
		params = (obj.id, obj.name, obj.email, obj.photo, obj.id)

		# run the query
		cursor = self.db.getCursor()
		rowsAffected = cursor.execute(query, params)
		cursor.close()

		if rowsAffected > 0:
			return True
		else:
			return False