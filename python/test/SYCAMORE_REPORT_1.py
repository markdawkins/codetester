#!/usr/bin/env python
import time
from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException

username = input('Enter your SSH username: ')
password = getpass()

#with open('commands_file') as f:
#    commands_list = f.read().splitlines()

filename = "/REPORTS/SYCAMORE/SYCAMORE_SITE_REPORT.csv" 

#file.write(' \n')
print ("Writing output to REPORTS directory...")
time.sleep(1)

file = open(filename , 'w')

with open('/LISTS/SYC_ROUTERS.txt') as f:
    devices_list = f.read().splitlines()

for devices in devices_list:
    print ('Connecting to device ' + devices)
    #ip_address_of_device = devices
    HOST = devices
    ios_device = {
        'device_type': 'cisco_ios',
        'ip': HOST, 
        'username': username,
        'password': password
    }

    try:
        net_connect = ConnectHandler(**ios_device)
    except (AuthenticationException):
        print ('Authentication failure: ' + HOST)
        continue
    except (NetMikoTimeoutException):
        print ('Timeout to device: ' + HOST)
        continue
    except (EOFError):
        print ('End of file while attempting device ' + HOST)
        continue
    except (SSHException):
        print ('SSH Issue. Are you sure SSH is enabled? ' + HOST)
        continue
    except Exception as unknown_error:
        print ('Some other error: ' + str(unknown_error) )
        continue

    output0 = net_connect.send_command('show run | inc hostname')
    output1 = net_connect.send_command('show ip int brie  | inc Serial')
    output2 = net_connect.send_command('show ip int brie  | inc 0/0/0')
    output2a = net_connect.send_command('show ip int brie  | inc 0/0/2')
    output3 = net_connect.send_command('show ip int brie  | inc Tunnel3')
    output4 = net_connect.send_command('show run | inc location')
    time.sleep(3)
    print (output0) 
    print (output1) 
    print (output2) 
    print (output2a)
    print (output3) 
    print (output4) 
    time.sleep(1)
    file.write(output0)
    file.write(' \n')
    file.write(' \n')
    file.write(output1)
    file.write(' \n')
    file.write(' \n')
    file.write(output2)
    file.write(' \n')
    file.write(' \n')
    file.write(output2a)
    file.write(' \n')
    file.write(' \n')
    file.write(output3)
    file.write(' \n')
    file.write(' \n')
    file.write(output4)
    file.write(' \n')
    file.write(' \n')
    net_connect.send_command('end\n')
    #file.close()
    print ("Report saved to Reports directory...")
    time.sleep(3)
