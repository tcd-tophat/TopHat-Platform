import metadataobjectmapper
import Model.usermetadata
import usermapper

class UserMetaDataMapper(metadataobjectmapper.MetaDataObjectMapper):

	def __init__(self):
		super(UserMetaDataMapper, self).__init__()

	def targetClass(self):
		return "UserMetaData"

	def tableName(self):
		return "users_meta"

	def objectColumnName(self):
		return "user_id"

	def _doCreateObject(self, data):
		"""Builds the UserMetaData objects from the data pulled from the database"""
		user_meta = Model.usermetadata.UserMetaData(data["id"])

		user_meta.setKey(data["key"])
		user_meta.setValue(value)

		# get the user object
		UM = usermapper.UserMapper()
		UserMapper = usermapper.UserMapper()
		user_ = UserMapper.find(data["user_id"])
		user_meta.setUser(user_)

		return user_meta