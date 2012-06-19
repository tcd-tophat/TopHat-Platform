#!/usr/bin/env python2.7
from Model.textresponse import TextResponse

from ssl import wrap_socket
from socket import socket
from sys import argv
from struct import pack, unpack, error as HeaderFormatError
def main():
		ver=2
		opcode=0
		res=0
		s = socket()
		s.connect((argv[1],int(argv[2])))
		s=wrap_socket(s)
		data="Hiya: \"hi\""
		uri="jsontest"
		urilen=len(uri)
		datalen=len(data)
		header=pack("BBHHH", ver, opcode, res, datalen, urilen)
		s.write(header)
		s.write(uri)
		s.write(data)


		header = self.recv(8)
		try:
			header=unpack("BBHHH", header)
		except HeaderFormatError:
			self.close()
			return 
		ver=header[0]
		
		if TopHatNetwork.ver is not ver:
			self.close()
			return

		opcode=header[1]
		res=header[2]
		datalen=header[3]
		urilen=header[4]
		uri=self.recv(urilen)
		data=self.recv(datalen)
		print "HEADER: %d %d %d %d \nURI: %s\nDATA: %s" % (opcode,res,datalen,urilen,uri,data)






if __name__ == '__main__':
		main()
		
