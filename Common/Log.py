from pathfinder.pathfinder import path
from os import listdir
import gzip
class LogFile:

	def __init__(self, filename='/var/log/tophat/tophat.log'):
		self.filename = filename
		self.path = path(filename)
	


	def write(self, messege):
		if  path(self.filename).exists:

			pass
		else: open(self.filename,'a').close()

		if self.path.size >= 524288: #512KB
			dirlist = listdir(self.path.realpath.parent.path)
			if self.path.basename in dirlist:
				i=1
				while True:
					new_name = self.path.realpath.parent.path +'/'+ self.path.basename + '.' + str(i) +'.'+'gz'
					if new_name in dirlist:
						pass
					else:
						uncmp = open(self.filename, 'rb')
						zipped = gzip.open(new_name, 'wb')
						zipped.writelines(uncmp)
						uncmp.close()
						zipped.close()
						break
				outfile = open(self.filename, 'w')
				outfile.write(messege)
				outfile.close()
				return
			else: 
				outfile = open(self.filename, 'a')
				outfile.write(messege)
				outfile.close()
				return
		else:
			outfile = open(self.filename, 'a')
			outfile.write(messege)
			outfile.close()
