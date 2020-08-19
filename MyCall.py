#Only termyx ..
import time
import subprocess

print('\033[1;31m' " __  __          ____      _ _")
print("|  \/  |_   _   / ___|__ _| | |")
print('\033[1;33m' "| |\/| | | | | | |   / _` | | |")
print('\033[1;33m' "| |  | | |_| | | |__| (_| | | |  _   _")
print('\033[1;31m' "|_|  |_|\__, |  \____\__,_|_|_| (_) (_)")
print("        |___/")
print("===========================================")

print("")

time.sleep(1)

try:
        x=input('\033[1;32m' "[+] Enter phone number :- ")

        y=" termux-telephony-call " +x

        subprocess.getoutput(y)
        print("")
        print('\033[1;35m' "Operation complete !¡ ")
except Exeption:

        print("plz turn on your mobile data ")
        time.sleep(1)

        subprocess.getoutput('pkg install termux-api -y')
        sibprocess.getoutput('pkg install python -y ')
        print("Now install Termux API app on app store")

#Code by Rush ..
#Ushan Rashmika