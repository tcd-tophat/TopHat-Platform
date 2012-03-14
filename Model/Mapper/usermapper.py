
class UserMapper(Mapper):

	def __init__(self):
		pass

	def targetClass(self):
		return "User"

	def __selectStmt(self):
		return "SELECT * FROM users WHERE id = ?"

	def __selectAllStmt(self, start, number):
		if(start < 1)
			print "The start point must be a positive int"
			start = 1

		if(number > 50)
			print "You cannot select more than 50 rows at one time"
			start = 50

		return "SELECT * FROM users LIMIT " + start + ", " + number	

	def __doCreateObject(self, data):
		pass

	def __doInsert(self, obj):
		print "Inserting new user object " + obj.id

	def __doDelete(self, obj):
		print "Deleting user " + obj.id

	def __doUpdate(self, obj):
		print "Updating user " + obj.id