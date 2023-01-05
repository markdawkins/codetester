from netmiko import ConnectHandler
import time
from getpass import getpass


host = input("Enter Host/IP: ")

user_name = input("Enter username:")
password = getpass("Enter password: ")
iosv_l2 = {
             'device_type':'cisco_ios',
             'host':host,
             'username':user_name,
             'password':password,
             
}
net_connect = ConnectHandler(**iosv_l2)

output = net_connect.send_command('show ver | inc uptime ')
print (output)
net_connect.send_command('end\n')




