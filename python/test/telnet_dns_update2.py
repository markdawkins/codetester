import telnetlib
from getpass import getpass
import time 

USER = input("username: ")
PASSWORD = getpass ("password:  ")

LIST = input("Enter List name: ")

listname = "./LISTs/%s.txt"  % LIST 

f = open (listname)

for line in f:
    HOST = line.strip()

    tn = telnetlib.Telnet(HOST)

    tn.read_until(b"Username: ")
    tn.write(USER.encode('ascii') + b"\n")

    tn.read_until(b"Password: ")
    tn.write(PASSWORD.encode('ascii') + b"\n")

    tn.write(b"conf t\n")
    tn.write(b"ip name-server 8.8.4.4\n ")
    tn.write(b" no ip name-server 192.168.250.210 \n")
    tn.write(b" end \n")
    time.sleep(2)
    tn.write(b" write mem\n")
    time.sleep(2)
    tn.close()

    print(" DNS configuration update completed ")
    time.sleep(2)
print (" Script completed ")
