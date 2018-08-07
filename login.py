#!/usr/bin/python

import getpass
import subprocess

def getUser():
    name = raw_input("Username:")
    return name

def getPassword():
    pw = getpass.getpass('Password:')
    return pw

def rdpLogin():
    name = getUser()
    pw = getPassword()
    cmd = "xfreerdp /v:192.168.0.170:3389 /u:{} /p:{} /d:dbs4pos /f /drives /usb /multimon".format(name, pw)
    print(cmd);
    subprocess.call([cmd], shell=True)
    
rdpLogin()

    



