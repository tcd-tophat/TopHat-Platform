SSLKeyPath=  'keys/tophat.key'

SSLCertPath= 'keys/tophat.crt'

SSLCAPath = 'keys/ca.crt'		

Port=443

Interface='0.0.0.0'

User='tophat'

Group='tophat'

Threads=6

EncryptionMethod=SSLEncryption

LogFile='/var/log/tophat/tophat.log'

DBDriver='MySQL'

MySQLHost='localhost'

MySQLUser='tophat'

MySQLPass='password'

MySQLDatabase='tophat'

resources = [
	('/apitokens/', "Apitokens")
	('/users/', "Users")
]