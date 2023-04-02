import csv
from getpass import getpass
from netmiko import ConnectHandler

# List of cisco switch IP addresses
ip = input("Enter switch ip:" )
#LIST = input("Enter List Name:")
#listname  = ".//LISTs//%s.txt"  % LIST

# Username and password to login to cisco switches

username = input("Enter Username: ")
password = getpass("Enter password: ")

#Output report name 

REPORT = input("Enter Report Name:")
# CSV file to write results to
output_file = ".//REPORTS//SWITCH_REPORTS//%s.csv" % REPORT

print('#' * 50)
# CSV header row
header = ["IP Address", "Interface status "]


# Open CSV file for writing
with open(output_file, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
                       
    
    device = {
                "device_type": "cisco_ios",
                "ip":ip,
                "username": username,
                "password": password,

            }
    #try:
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command("show ip interface brief")
    net_connect.disconnect()

    # Extract connnected interface values from output
    int_status = output.split(":")[-1].strip()

    # Write result to CSV file
    writer.writerow([ip, int_status])
            

#Exception as e:
#print(f"Error connecting to {ip}: {str(e)}")
