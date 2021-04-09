#Credit : FM#9999

import os, time, sys
from time import sleep

#os,sys pour system ,time ,colorama pour le temps,commande systeme,couleur 

password = "Division 21"

#cls = clear les element sur la console

time.sleep(0)
passtry=input("P4ssw0rd : ")
os.system("cls")
if passtry == password:
    
    print ("Code Bon")
    time.sleep(1)
    os.system("cls")
    print("Quelle est votre choix ?")
    print("1 - SQL sniper")
    print("2 - Soon...")
    choix = input("Quelle est choix : ")
    if choix == "1":
        os.system("cls")
        print ("SQLMAP has been selected")
        print("Mise a jour des paquets")
        os.system("sudo apt-get update -y")
        os.system("sudo apt-get install sqlmap")
        url=input("What's url website? : ")
        os.system("sqlmap", url, "--dump-all")
    elif choix == "2":
        os.system("cls")
        print("Soon...")
    else:                 
        print("ERROR:101") #Error:101 signifie que la saisie n'est pas correcte tel que un code
else:
    print("Wrong password")
    print("")
    print("Join discord : http://division21.42web.io/discord.html")
    print("")