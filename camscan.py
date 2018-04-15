#!/usr/bin/python3
import socket
import subprocess as sp
import os
import lib.ipscaner as ips
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
def testip(ip,port):
	if ips.scan(ip,port):
		goodip.append(ip+':'+port)
		print('found '+ip+' '+port)
	else:
		print('')

def main():
	dload()
	testconstants()

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		exit()
