import telnetlib
from getpass import getpass
import time 

HOST = input("router_ip_address: " )
USER = input("username: ")
PASSWORD = getpass ("password:  ")

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(USER.encode('ascii') + b"\n")

tn.read_until(b"Password: ")
tn.write(PASSWORD.encode('ascii') + b"\n")

tn.write(b"conf t\n")
tn.write(b"ip name-server 8.8.8.8\n ")
tn.write(b" end \n")
#output = tn.read_until(b"443")
#print(output.decode('ascii'))
time.sleep(2)
tn.write(b" write mem\n")
time.sleep(2)
tn.close()

print(" DNS configuration update completed ")
time.sleep(5)
