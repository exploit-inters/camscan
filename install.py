#!/usr/bin/python3
import subprocess as sp
import os


sp.call('pip install -r requirements.txt',shell=True) 
sp.call('rm -fr requirements.txt',shell=True) 
sp.call('rm -fr install.py',shell=True)
os.system('rm -fr README.md .git/ ')
