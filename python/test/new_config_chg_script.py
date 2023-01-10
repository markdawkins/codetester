#!/usr/bin/env python
from getpass import getpass
import time
from netmiko import ConnectHandler

username = input("Enter username: ")
password = getpass()
LIST = input("Enter List name: ")

listname = "/LISTS/%s.txt"  % LIST

f = open (listname)

for line in f:
    host = line.strip()
    iosv_l2 = {
             'device_type':'cisco_ios',
             'ip':host,
             'username': username,
             'password': password,
           }

    net_connect = ConnectHandler(**iosv_l2)
    net_connect.send_command_timing('conf t\n')
    net_connect.send_command_timing('ip name-server 192.168.250.210\n')
    net_connect.send_command_timing('no ip name-server 192.165.250.210\n')      
    net_connect.send_command_timing('end\n')
    net_connect.send_command_timing('wr mem\n')
    time.sleep(3)
    output0 = net_connect.send_command_timing('show run | inc hostname\n')
    time.sleep(1)
    output1 = net_connect.send_command_timing('show run | inc ip name-server\n')
    time.sleep(1)
    print(" ")
    print("The DNS Server configuration has been updated for device " + output0[8:20] + " " + host )
    print(" ")
    print(output1)
    print (" ")

print ("Update completed for all devices...")
time.sleep(10)
