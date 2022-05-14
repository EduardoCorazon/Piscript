'''
Made by: MercenaryHarpy6
Date:5/11/2022
Description: Simple script that logs into my pi via ssh and runs whatever I want scripts
'''
#!/usr/bin/env python3

# imports
from config import *
import subprocess
import itertools
from threading import Thread
import time
import sys


def localdetail():
    # check if windows or linux
    if sys.platform == "linux" OR "linux2"
    localinfo = subprocess.run("ifconfig -a | grep 'broadcast'", shell=True,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print("Your network information is: \n" +
          localinfo.stdout + "You are running: ")


def info():
    if username != '':
        print("Using configfile...\n")
        info.RemoteUser = username
        info.RemoteIP = remotehost

    else:

        info.RemoteUser = str(input("Input Remote machine username: "))
        info.RemoteIP = str(input("Input Remote machine IP: "))
    info.target = str(input("Input the target IP: "))
    print("If no commands are passed in, an nmap scan will be performed")
    info.command = str(
        input("input command you want to run here [for default leave empty]:"))
    defaultcommand()


def defaultcommand():
    if (info.command == ''):
        print(
            "An nmap scan will now be done\nPlease wait while the scan is being performed")
        info.command = "msfconsole && nmap -A -vv {target}".format(
            target=info.target)
    return(info.command)


def waitanimation():
    if loginserver.waiting == False:
        for i in itertools.cycle(["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]):
            if loginserver.waiting == True:
                print("done!")
                break
            sys.stdout.write('\rloading ' + i)
            sys.stdout.flush()
            time.sleep(0.1)


def loginserver():
    loginserver.waiting = False
    login = subprocess.run("ssh {user}@{host} {cmd}".format(user=info.RemoteUser, host=info.RemoteIP,
                           cmd=info.command), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    loginserver.waiting = True
    print(login.stdout)


if __name__ == '__main__':
    localdetail()
    info()
    Thread(target=loginserver).start()
    Thread(target=waitanimation).start()
