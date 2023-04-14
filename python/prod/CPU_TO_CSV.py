import csv
import paramiko
import socket

LIST = input("Enter list:")
REPORT = input("Enter Report Name:")
#from getpass import getpass
#passwd = getpass("Enter password: ")

listname = "\LISTS\%s.txt"  % LIST
cpu_report = "\REPORTS\CPU_REPORTS\%s.csv" % REPORT


# Define the CSV file name and headers
csv_file = '\REPORTS\CPU_REPORTS\switch_cpu.csv'


csv_headers = ['Switch IP', 'CPU Utilization']

# Read the list of switch IPs from an external file
with open(listname , 'r') as f:
    switch_ips = [line.strip() for line in f]

# Open the CSV file and write the headers
with open(cpu_report, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(csv_headers)

    # Loop through the list of switch IPs
    for switch_ip in switch_ips:
        try:
            # Connect to the switch using SSH
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(switch_ip, username='admin', password='passwordgoeshere')

            # Run the "show proc cpu" command and get the output
            stdin, stdout, stderr = client.exec_command('show proc cpu  | inc five minutes')
            output = stdout.read().decode()

            # Write the switch IP and CPU utilization to the CSV file
            writer.writerow([switch_ip, output.strip()])

            # Close the SSH connection
            client.close()

        except (paramiko.ssh_exception.AuthenticationException,
                paramiko.ssh_exception.SSHException,
                socket.error) as e:
            # If the switch is unreachable, print an error message and continue to the next IP
            print(f'Error connecting to {switch_ip}: {e}')
            continue
