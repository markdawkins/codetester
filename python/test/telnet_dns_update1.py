import telnetlib
from getpass import getpass


HOST = input("router_ip_address: " )
USER = input("username: ")
PASSWORD = getpass ("password:  ")

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(USER.encode('ascii') + b"\n")

tn.read_until(b"Password: ")
tn.write(PASSWORD.encode('ascii') + b"\n")

tn.write(b"show run\n")
output = tn.read_until(b"443")
print(output.decode('ascii'))

tn.write(b"exit\n")
tn.close()
