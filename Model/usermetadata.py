import metadatobject
import user
import domainexception

class UserMetaData(metadatobject.MetaDataObject):

	__user = None # reference to the User object to which this object is attached

	def __init__(self, id=None, user=None):
		if type(user) is not user.User:
			self.__user = user

		super(UserMetaData, self).__init__(id)

	def setUser(self, user):
		if is not isinstance(user, user.User):
			raise domainexception.DomainException("User attribute must be a reference to a User object")

		self.__user = user

	def getUser(self):
		return self.__user