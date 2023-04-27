#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass
from time import sleep

#device_name = input("Enter device name: ")
username = input("Enter username: ")
 
HOST = input("Enter host IP: ")

iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip':(HOST),
    'username': username,
    'password': getpass('Enter SSH password: '),
}

net_connect = ConnectHandler(**iosv_l2)
sleep(1)
net_connect.send_command('\n')

#net_connect.find_prompt()
output = net_connect.send_command('show ip interface brief')
sleep(1)
output1 = net_connect.send_command('show cdp nei | inc SEP')
sleep(1)
output2 = net_connect.send_command('show ver')
sleep(3)
output3 = net_connect.send_command('show mac address-table ')
sleep(.5)
output4 = net_connect.send_command('show interface | include (is  up|rate )')
sleep(.5)
output5 = net_connect.send_command('show log | inc FAILED')
sleep(1)
output6 = net_connect.send_command('show cdp nei')

print (output) 
print (" ")
print (output1)
print (" ")
print (output2) 
print (" ")
print (output3) 
print (" ")
print (output4) 
print (" ")
print (output5)   
print (" ")
print (output6)

net_connect.send_command('end\n')
