#!/usr/bin/env python
from getpass import getpass
import time
from netmiko import ConnectHandler

from netmiko import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko import NetmikoAuthenticationException

username = input("Enter username: ")
password = getpass()
LIST = input("Enter List name: ")

listname = "/LISTs/%s.txt"  % LIST 

f = open (listname)

for line in f:
    host = line.strip()
    iosv_l2 = {
             'device_type':'cisco_ios',
             'ip':host,
             'username': username,
             'password': password,
           }
         
    try:
      net_connect = ConnectHandler(**iosv_l2)
    except (NetmikoAuthenticationException):
        print ('Authentication failure: ' + str(host))
        continue
    except (NetMikoTimeoutException):
        print ('Timeout to device: ' + str(host))
        continue
    except (EOFError):
        print ("End of file while attempting device " + str(host))
        continue
    except (SSHException):
        print ('SSH Issue. Are you sure SSH is enabled ? ' + str(host))
        continue
    except Exception as unknown_error:
        print ('Some other error or end of script: ' + str(unknown_error))
        continue
   
    net_connect.send_command_timing('conf t\n')
    net_connect.send_command_timing('ip name-server 192.168.250.210\n')
    net_connect.send_command_timing('no ip name-server 192.165.250.210\n')      
    net_connect.send_command_timing('end\n')
    net_connect.send_command_timing('wr mem\n')
    time.sleep(1)
    output1 = net_connect.send_command_timing('show run | inc ip name-server')
    time.sleep(1)
    print(" ")
    output2 = net_connect.send_command_timing('show run | inc hostname')
    time.sleep(1)
    print("The DNS Server configuration has been updated for the device  at ip address " + " " + host + output2[8:16])
    print(" ")
    print(output1)
    print(" ")
    
print ("Update completed for all devices...")
time.sleep(1)
