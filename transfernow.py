'''
Made by: MercenaryHarpy6
Date:5/11/2022
Description: Simple script that logs into my pi via ssh and runs whatever I want scripts
'''
#!/usr/bin/env python3

#imports
import subprocess



def info():
    info.RemoteUser = str(input("Input Remote machine username: "))
    info.RemotePass = str(input("Input Remote machine password: "))
    print("If no commands are passed in, an nmap scan and metsploit will be started; if a common services is found running then it will be searched in metasploit")
    info.command = str(input("input command you want to run here [for default leave empty]:"))
    

def loginserver():
    login = subprocess.run("ssh {user}@{host} {cmd}".format(user=info.RemoteUser, host=info.RemotePass, cmd='nmap -A '), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    







if __name__ == '__main__':
    info()
    #loginserver()
    
