import metadataobject
import user
import domainexception

class UserMetaData(metadataobject.MetaDataObject):

	_user = None # reference to the User object to which this object is attached

	def __init__(self, id_=None, user_=None, key=None, value=None):
		if not None:
			self.setUser(user_)

		self.setKey(key)
		self.setValue(value)

		super(UserMetaData, self).__init__(id_)

	def setUser(self, user_):
		if not isinstance(user_, user.User):
			raise domainexception.DomainException("User attribute must be a reference to a User object")

		self._user = user_

		# add reference in the User object to this object
		self._user.addMetaData(self)

	def getUser(self):
		return self._user