#!/usr/bin/env python2.7
from Model.textresponse import TextResponse

from ssl import wrap_socket
from socket import socket
from sys import argv
from struct import pack, unpack, error as HeaderFormatError
def main():
		ver=2
		opcode=2
		res=0
		s = socket()
		s.connect((argv[1],int(argv[2])))
		s=wrap_socket(s)
		data="Hiya: \"hi\""
		uri="blackbird://test"
		urilen=len(uri)
		datalen=len(data)
		header=pack("BBHHH", ver, opcode, res, datalen, urilen)
		s.write(header)
		s.write(uri)
		s.write(data)






if __name__ == '__main__':
		main()
		
