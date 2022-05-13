'''
Made by: MercenaryHarpy6
Date:5/11/2022
Description: Python smb file share
'''
#!/usr/bin/env python3

#imports
from config import *
import subprocess
import sys
#consider using paramiko?

def serversetup():
    #login = subprocess.run("ssh {user}@{host} {cmd}".format(user=RemoteUser, host=RemotePass, cmd='ls -l'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    

    #checks if there was an error
    '''
    if login.returncode != 0:
        print("\nfThere was an error")
        print(login.stderr)
    '''
    subprocess.run(['powershell.exe', 'New-SmbShare', '-Path', 'C:\\Users\\ ', '-Name', 'ShareFile']) # creates a share file on Server PC




if __name__ == '__main__':
    serversetup()
    
