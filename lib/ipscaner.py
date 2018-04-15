#!/usr/bin/python3
import socket
def scan(ip,p):
	host = str(ip)
	port = int(p)
	timeout = 5
	args = socket.getaddrinfo(host, port, socket.AF_INET, socket.SOCK_STREAM)
	for family, socktype, proto, canonname, sockaddr in args:
		s = socket.socket(family, socktype, proto)
		socket.setdefaulttimeout(timeout)
		try:
			s.connect(sockaddr)
		except:
			return False
		else:
			s.close()
			return True

if __name__ == '__main__':
	exit()
