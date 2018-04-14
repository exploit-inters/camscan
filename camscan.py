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
_version_ = "2.0 release"
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

	
	
		
def main():
	pass
if __name__ == "__main__":
	main()
