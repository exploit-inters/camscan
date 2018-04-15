#!/usr/bin/python3
import subprocess as sp
import os


sp.call('pip install -r requirements.txt',shell=True) 
sp.call('rm -fr requirements.txt',shell=True) 
sp.call('rm -fr install.py',shell=True)
os.system('rm -fr README.md .git/ ')
print('install finished!\n')
a = input('start program? (y or n): ')
a.upper()
if a == 'Y':
  os.system('python3 camscan.py')
elif a == 'N':
  exit()
print('123')

