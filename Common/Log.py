from pathfinder.pathfinder import path
from os import listdir
import gzip
class LogFile:

	def __init__(self, filename='/var/log/tophat/tophat.log'):
		print "Creating log object"
		self.filename = filename
		self.path = path(filename)
	


	def write(self, messege):
		if  path(self.filename).exists:

			pass
		else: open(self.filename,'a').close()

		if self.path.size >= 524288: #512KB
			dirlist = listdir(self.realpath.parent.path)
			if filename in dirlist:
				i=0
				while True:
					new_name = self.realpath.parent.path + filename + '.' + str(i) +'gz'
					if new_name in dirlist:
						pass
					else:
						uncmp = open(self.filename, 'rb')
						zipped = gzip.open(new_name, 'wb')
						zipped.writelines(uncmp)
						uncmp.close()
						zipped.close()
						break
				outfile = open(filename, 'w')
				outfile.write(messege)
				outfile.close()
				return
			else: 
				outfile = open(filename, 'a')
				outfile.write(messege)
				outfile.close()
				return
		else:
			outfile = open(self.filename, 'a')
			outfile.write(messege)
			outfile.close()
