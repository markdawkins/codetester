from netmiko import ConnectHandler
import csv

LIST = input("Enter list:")
REPORT = input("Enter Report Name:")
from getpass import getpass
passwd = getpass("Enter password: ")

listname = "\LISTS\%s.txt"  % LIST
cpu_report = "\REPORTS\CPU_REPORTS\%s.csv" % REPORT

# Read in the switch IP addresses from the external file
with open(listname , mode='r') as file:
    switch_ips = file.read().splitlines()

# Define the SSH connection parameters for the switches
device_params = {
    'device_type': 'cisco_ios',
    'username': 'admin',
    'password': passwd
}

# Create a CSV file to store the output
with open(cpu_report + '.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Hostname', 'CPU Processor  Output'])

    # Connect to each switch and run the command
    for ip in switch_ips:
        device_params['ip'] = ip
        with ConnectHandler(**device_params) as ssh:
             prompt = ssh.find_prompt()
             output = ssh.send_command('show proc cpu')
             hostname = prompt
             
        # Write the output to a new line in the CSV file
        writer.writerow([hostname, output ])
