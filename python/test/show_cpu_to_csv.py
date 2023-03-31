import csv
from getpass import getpass
from netmiko import ConnectHandler

# List of cisco switch IP addresses
LIST = input("Enter List Name:")
listname  = "./LISTS/%s.txt"  % LIST

# Username and password to login to cisco switches

username = input("Enter Username: ")
password = getpass("Enter password: ")

#Output report name 

REPORT = input("Enter Report Name:")
# CSV file to write results to
output_file = "./REPORTS/CPU_REPORTS/%s.csv" % REPORT

# CSV header row
header = ["IP Address", "CPU Utilization"]

# Open CSV file for writing
with open(output_file, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
                       
    f = open (listname)
    # Connect to each switch and run command
    for ip in f:
        device = ip.strip()
        device = {
            "device_type": "cisco_ios",
            "ip":device,
            "username": username,
            "password":password,

        }
        try:
            net_connect = ConnectHandler(**device)
            output = net_connect.send_command("show processes | inc CPU utilization")
            net_connect.disconnect()

            # Extract CPU utilization value from output
            cpu_utilization = output.split(":")[-1].strip()

            # Write result to CSV file
            writer.writerow([ip, cpu_utilization])

        except Exception as e:
            print(f"Error connecting to {ip}: {str(e)}")
