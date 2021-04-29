#Credit : FM#1234

import os
import time
import sys
import bdb
import distutils
import glob
import inspect
import json
import logging
import os
import re
import shutil
import sys
import tempfile
import threading
import time
import traceback
import warnings



from time import sleep


password = "Division 21"


time.sleep(0)
passtry=input("P4ssw0rd : ")
os.system("clear")
if passtry == password:
    
    print("Correct password")
    time.sleep(0.5)
    os.system("cls")
    print("Redirecting...")
    time.sleep(0.5)
    os.system("clear")
    print("Menu")
    print("1 - SQL sniper")
    print("2 - Soon...")
    choix = input("Choice : ")
    
    
    if choix == "1":
        os.system("clear")
        print ("SQLMAP has been selected")
        print("Updating your packages...")
        time.sleep(1)
        os.system("sudo apt-get update -y")
        os.system("clear")
        os.system("sudo apt-get install sqlmap")
        os.system("clear")
        os.system("sudo apt --fix-broken install")
        url=input("What's url website? : ")
        os.system("sqlmap" + url + "--dump-all")
    elif choix == "2":
        os.system("clear")
        print("Soon...")
    else:                 
        print("Answer!")

else:
    print("Wrong password")
    print("")
    print("Join discord : http://division21.42web.io/discord.html")
    print("")
