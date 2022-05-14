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
    info.RemoteIP = str(input("Input Remote machine IP: "))
    info.target = str(input("Input the target IP: "))
    print("If no commands are passed in, an nmap scan and metsploit will be started; if a common services is found running then it will be searched in metasploit")
    info.command = str(input("input command you want to run here [for default leave empty]: \n"))
    if (info.command == ''):
        info.command = "msfconsole && nmap -Pn {target}".format(target=info.target)
    return(info.command)
    

def loginserver():
    login = subprocess.run("ssh {user}@{host} {cmd}".format(user=info.RemoteUser, host=info.RemoteIP, cmd=info.command), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(login.stdout)

if __name__ == '__main__':
    info()
    loginserver()
    
