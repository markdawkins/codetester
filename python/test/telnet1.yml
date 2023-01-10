import telnetlib

HOST = "router_ip_address"
USER = "username"
PASSWORD = "password"

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(USER.encode('ascii') + b"\n")

tn.read_until(b"Password: ")
tn.write(PASSWORD.encode('ascii') + b"\n")

tn.write(b"show run\n")
output = tn.read_until(b"end")
print(output.decode('ascii'))

tn.write(b"exit\n")
tn.close()
