import metadataobject
import user
import domainexception

class UserMetaData(metadataobject.MetaDataObject):

	def __init__(self, id_=None):
		super(UserMetaData, self).__init__(id_)

	def _doSetObject(self, user_):
		if not isinstance(user_, user.User):
			raise domainexception.DomainException("User attribute must be a reference to a User object")

		self._object = user_

	def getObject(self):
		return self._object