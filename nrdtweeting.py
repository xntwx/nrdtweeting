# code by nur tri wibowo [nurtri@gmx.com]
#
# github.com/xntwx
#
# twitter activity using python with library from sixohsix [http://mike.verdone.ca/twitter/]
#

import sys
import os
from twitter import *

twit = Twitter(auth = OAuth('Access-Token','Access-Token-Secret',
                            'API-Key','API-Secret')
               )

def cls():
    os.system(['clear','cls'][os.name == 'nt'])

def menu():
    try:
        print ("1. Update Status \n2. Send Direct Message \n3. Exit \n\n nordskriving.wordpress.com \n")
        pil = input("Enter your choice: ")

        if not pil:
            menu()
        elif pil == "1":
            upd_status()
        elif pil == "2":
            dm()
        elif pil == "3":
            sys.exit()
        else:
            cls()
            menu()
    except KeyboardInterrupt:
        sys.exit()

def upd_status():
    cls()
    try:
        stat = input("Status: ")

        if not stat:
            cls()
            upd_status()
        else:
            twit.statuses.update(status = stat + " [using @nordskriving's app]")
            print ("\nComplete!\n")
            menu()
    except KeyboardInterrupt:
        sys.exit()

def dm():
    cls()
    try:
        forwho = input("Friend's id: ")
        txt    = input("Text       : ")

        if not forwho or not txt:
            cls()
            dm()
        else:
            twit.direct_messages.new(user = forwho, text = txt + " [send using @nordskriving's app]")
            print ("\n \nComplete!\n")
            menu()
    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__":
    cls()
    menu()

