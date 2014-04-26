# Automate your setups with the following API's
# This could have bug, share if you can come up with useful API's
# Please get your hands dirty in python to solve the issues, if you find one

from subprocess import call
import subprocess 
import sys
import time
import inspect, os, sys
from optparse import OptionParser




def decorateScreenStringWindow(screenname, id, a):
    return  "screen -x " + screenname + " -p"+ str(id) +" -X stuff " +"'"+   a + "\r'"

def decorateDefaultString( screenname, a):
    return "screen -x  " +  screenname  + " -X " + a 

def create_screen(sname, windowname = "bash"):
    createscreen = ["screen -d -m -S "+ sname + " -t " + windowname]
    p = subprocess.Popen(createscreen,shell=True)

def run_cmd_screen(sname, id, command):
    cmd = [decorateScreenStringWindow(sname, id, command)]
    subprocess.Popen(cmd, shell=True)
    time.sleep(0.3)
 
def create_window(sname, windowname):
    cmd = [decorateDefaultString(sname, " screen -t \"" + windowname + "\" ")]
    subprocess.Popen(cmd, shell=True)
    time.sleep(0.2)
        
