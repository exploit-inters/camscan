#!/usr/bin/python3
import socket
import subprocess as sp
import os
from lib.ipscaner import *
from lib.test import *
import sys
import random
import time as t
try:
	from netaddr import IPNetwork
	import requests
except ModuleNotFoundError:
	print("будласка встановіть бібліотеки\npip install -r requirements.txt\n")
	exit()

#------------------
_version_ = "1.0 beta"
hostsfile = "hosts.txt"
goodip = []
diapazons = []
ports = ['554']
ipcam = []
#------------------
def testconstants():
	print(_version_,hostsfile,ports,diapazons,goodip,ipcam)

def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()
def dload():
	f = open(hostsfile, 'r')
	for line in f:
		l = line.strip()
		diapazons.append(str(l))
	f.close()
	return
def ipcheck(ip,port):
	if scan(ip,port):
		goodip.append(ip+':'+port)
		print('found '+ip+' '+port)
	else:
		print('')
		
def start():
	if diapazons == []:
		print("diapazons error")
		t.sleep(0.4)
		restart_program()
	print("")
	for d in diapazons:
		if d == "\n":
			break
			
		else:
			print("for " + d)
			for ip in IPNetwork(d).iter_hosts():
				t.sleep(0.2)
				for p in ports:
					t.sleep(0.1)
					ipcheck(str(ip),str(p))

def main():
	dload()
	start()

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		exit()
