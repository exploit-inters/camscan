#!/usr/bin/python3
import socket
import subprocess as sp
import os
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
portsfile = "ports.txt"
hostsfile = "hosts.txt"
goodip = []
diapazons = []
ports = []
#------------------
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

def pload():
	f = open(portsfile, 'r')
	for line in f:
		l = line.strip()
		ports.append(str(l))
	f.close()
	return


def main():
	pload()
	dload()
if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		exit()
