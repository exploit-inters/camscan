
import socket
import subprocess as sp
import os
import sys
import random
import time as t
try:
	from netaddr import *
	import requests
except ModuleNotFoundError:
	print("будласка встановіть бібліотеки\npip install -r requirements.txt\n")
	exit()
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
