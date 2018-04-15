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

def test(t):
	print(t)
