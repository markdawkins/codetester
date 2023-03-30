import csv
from getpass import getpass
from netmiko import ConnectHandler

LIST = input("Enter List Name:")
#ip_list = "\LISTS\%s.txt"  % LIST

# List of Cisco switch IP addresses
ip_list = ["10.12.95.245", "10.12.95.247", "10.12.95.246"]
username = input("Enter Username: ")
password = getpass("Enter password: ")

REPORT = input("Enter Report Name:")
# CSV file to write results to
output_file = "\REPORTS\CPU_REPORTS\%s.csv" % REPORT

# CSV header row
header = ["IP Address", "CPU Utilization"]

# Open CSV file for writing
with open(output_file, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)

    # Connect to each switch and run command
    for ip in ip_list:
        device = ip.strip()
        device = {
            "device_type": "cisco_ios",
            "ip": ip,
            "username": "svc_ansible",
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
