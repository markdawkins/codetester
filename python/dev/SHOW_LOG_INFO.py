import time
from netmiko import ConnectHandler
from getpass import getpass
from netmiko import ConnectHandler
from datetime import datetime

username = input("Enter username: ")
password = getpass('Enter SSH password: ')
host_ip  = input("Enter host IP: ")
date1 = input("Enter Month: ")
date2 = input("Enter Day: ")
#date3 = input("Enter Year: ")
#date4 = input("Enter Time: ")
#date_complete = (date1 + (" ") + date2 + (" ") + date3 + (" "))
date_complete = (date1 + (" ") + date2 + (" "))

show_command_1 = ("show log | inc " + date_complete)
#show_command_2 = input("Enter command 2:")

subname = datetime.now().strftime("%Y%m%d-%H%M%S")
#LIST = input("Enter Floor - e.g. north_south_idf_stacks , idf_south, idf_north , sports_complex:")
reportname = "/REPORTS/general_report/command-" + subname + ".txt"
#listname = "/LISTS/%s.txt" % LIST

print ("Writing output to REPORTS directory...")
time.sleep(3)

file = open(reportname , 'w')

#f = open (listname)

#for line in f:
host = (host_ip)
iosv_l2 = {
            'device_type':'cisco_ios',
            'ip':host,
            'username':username,
            'password':password,
        }
#try:
#    net_connect = ConnectHandler(**iosv_l2)
#except (AuthenticationException):
#    print ('Authentication failure: ' + HOST)
#    continue
#except (NetMikoTimeoutException):
#    print ('Timeout to device: ' + HOST)
#    file.write('Timeout to device: ' + HOST)
#    continue
#except (EOFError):
#    print ('End of file while attempting device ' + HOST)
#    continue
#except (SSHException):
#    print ('SSH Issue. Are you sure SSH is enabled? ' + HOST)
#    continue
#except Exception as unknown_error:
#    print ('Some other error: ' + str(unknown_error) )
#    continue
net_connect = ConnectHandler(**iosv_l2)
output0 = net_connect.send_command('show run | inc hostname')
print (host + "\n")
file.write(host + "\n")
file.write( "\n")
print (output0[8:32])
file.write( "\n")
file.write (output0[8:32])
file.write( "\n")
file.write(" ")
file.write(" ")
file.write( "\n")    
net_connect = ConnectHandler(**iosv_l2)
output1 = net_connect.send_command(show_command_1)
print (output1)
file.write( "\n")
file.write (output1)
file.write( "\n")
file.write(" ")
file.write(" ")
file.write( "\n")
#output2 = net_connect.send_command(show_command_2)
#print (output2 + "\n")
#file.write( "\n")
#file.write (output2)
#file.write(" \n")
#file.write(" ")
#file.write(" \n")
    
file.close()

print ("Report saved to Reports directory...")
time.sleep(60)
