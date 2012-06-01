from abc import ABCMeta, abstractmethod
import mapper
import metadataobject

class MetaDataObjectMapper(mapper.Mapper):
	__metaclass__ = ABCMeta

	def __init__(self):
		super(MetaDataObjectMapper, self).__init__()

	def _selectStmt(self):
		return "SELECT * FROM " + self.tableName() + " WHERE id = %s LIMIT 1"

	def _selectAllStmt(self):
		return "SELECT * FROM " + self.tableName() + " LIMIT %s, %s"	

	def _doInsert(self, obj):
		if not isinstance(obj, metadataobject.MetaDataObject):
			raise mappererror.MapperError("You must give a MetaDataObject")

		# build query
		# id, name, photo, game_id, user_id, lat, lon, score, time
		query = "INSERT INTO " + self.tableName() + " VALUES(NULL, %s, %s, %s)"
		# build tuple of the parameters
		params = (obj.getObject(), obj.getKey(), obj.getValue())

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

	def _doDelete(self, obj):
		pass

	def _doUpdate(self, obj):
		if not isinstance(obj, metadataobject.MetaDataObject):
			raise mappererror.MapperError("You must give a MetaDataObject")

		# build the query
		query = "UPDATE " + self.tableName() + " SET " + self.objectColumnName() + " = %s, key = %s, value = %s WHERE id = %s LIMIT 1"
		params = (obj.getObject(), obj.getKey(), obj.getValue(), obj.getId())

		# run the query
		cursor = self.db.getCursor()
		rowsAffected = cursor.execute(query, params)
		cursor.close()

		if rowsAffected > 0:
			return True
		else:
			return False

	@abstractmethod
	def objectColumnName(self):
		pass