import subprocess as sp
import os

os.system('rm -fr README.md .git/ ')
sp.call('pip install -r requirements.txt',shell=True)

