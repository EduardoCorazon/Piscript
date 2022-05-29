'''
Made by: MercenaryHarpy6
Date:5/11/2022
Description: 
This is a simple test script to play around with for very simple practice, nothing important
Simple script that logs into my pi via ssh and runs whatever scripts I want
By default it will run an nmap scan on the target machine
'''
#!/usr/bin/env python3

# imports
from config import *
import socket
import subprocess
import itertools
from threading import Thread
import time
import sys


def localdetail():
    # check if windows or linux, this is so we can use the right network command later
    print("-------------------------------------------------")
    print("You are running a " + sys.platform + " system.")
    # datermine if we use ip or if config
    if sys.platform != "win32":
        net = "ifconfig -a | grep 'broadcast'"
    else:
        net = "ipconfig"
        print("Your device IP address is: " + socket.gethostbyname(socket.gethostname()))

    # This will display the systems network information
    localinfo = subprocess.run(net, shell=True,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print("Your network information is: \n" + localinfo.stdout)
    print("-------------------------------------------------")


def info():
    # set the variabels stored in the config file if any
    if username != '':
        print("Using configfile...\n")
        info.RemoteUser = username
        info.RemoteIP = remotehost

    else:
        #if the config file is empty, then request information from the user
        info.RemoteUser = str(input("Input Remote machine username: "))
        info.RemoteIP = str(input("Input Remote machine IP: "))
    info.target = str(input("Input the target/victim IP: "))
    print("If no commands are passed in, an nmap scan will be performed in background")
    info.command = str(
        input("input command you want to run here [for default leave empty]:"))
    defaultcommand()


def defaultcommand():
    #this is the command that will run if no comman is typedin in the info()
    #By deafults it will start metasploit and run an nmap scan on the target
    if (info.command == ''):
        #change the code below to whatever you like
        print(
            "An nmap scan will now be done\nPlease wait while the scan is being performed") 
        info.command = "nmap -A -vv {target}".format(
            target=info.target)
    return(info.command)


def waitanimation():
    #Loading/Waiting Animation for when the command is running
    if loginserver.waiting == False:
        for i in itertools.cycle(["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]):
            if loginserver.waiting == True:
                print("done!")
                break
            sys.stdout.write('\rloading ' + i)
            sys.stdout.flush()
            time.sleep(0.1)
            
def loginserver():
        #logs into Pi and runs the commands
        loginserver.waiting = False
        login = subprocess.run("ssh {user}@{host} {cmd}".format(user=info.RemoteUser, host=info.RemoteIP,
                           cmd=info.command), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        loginserver.waiting = True
        print(login.stdout)
        


#---------------------Main Program---------------------
if __name__ == '__main__':
    localdetail()
    info()
    Thread(target=loginserver).start()
    Thread(target=waitanimation).start()
