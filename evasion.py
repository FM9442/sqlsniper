#Credit : FM#1234

import os, time, sys
from time import sleep


password = "Division 21"


time.sleep(0)
passtry=input("P4ssw0rd : ")
os.system("cls")
if passtry == password:
    
    print("Correct password")
    time.sleep(0.5)
    os.system("cls")
    print("Redirecting...")
    time.sleep(0.5)
    os.system("cls")
    print("Menu")
    print("1 - SQL sniper")
    print("2 - Soon...")
    choix = input("Choice : ")
    
    
    if choix == "1":
        os.system("cls")
        print ("SQLMAP has been selected")
        print("Updating your packages...")
        os.system("sudo apt-get update -y")
        os.system("sudo apt-get install sqlmap")
        os.system("sudo pip3 install -r requirements.txt")
        url=input("What's url website? : ")
        os.system("python " " sqlmap ", url, " --dump-all")
    elif choix == "2":
        os.system("cls")
        print("Soon...")
    else:                 
        print("Answer!")

else:
    print("Wrong password")
    print("")
    print("Join discord : http://division21.42web.io/discord.html")
    print("")
