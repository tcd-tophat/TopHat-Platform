SSLKeyPath=  'keys/tophat.key'

SSLCertPath= 'keys/tophat.crt'

SSLCAPath = 'keys/ca.crt'		

Port=443

Interface='0.0.0.0'

User='tophat'

Group='tophat'

Threads=6

from Networking.Protocols.Twisted.Encryption.sslencryption import SSLEncryption

#from Controllers.Encryption.plaintext import Plaintext

EncryptionMethod =SSLEncryption

LogFile='/var/log/tophat/tophat.log'

DBDriver='MySQL'

MySQLHost='localhost'

MySQLUser='tophat'

MySQLPass='password'

MySQLDatabase='tophat'

