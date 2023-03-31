import paramiko
import time

# Define the access point's IP address, username, and password
ap_ip = '10.62.95.165'
ap_username = 'admin'
ap_password = 'afjlrty1463rm3m'

# Define the command to execute
command = 'archive download-sw /no-reload sftp://192.168.2.167/ap1g7'
command2 = 'username:apdl'
command3 = 'password:gEQAAp3C'


# Connect to the access point
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ap_ip, username=ap_username, password=ap_password )

# Execute the command
stdin, stdout, stderr = ssh.exec_command(command ,  get_pty=True)
stdin, stdout, stderr = ssh.exec_command('\n')
stdin, stdout, stderr = ssh.exec_command(command2 , get_pty=True)
stdin, stdout, stderr = ssh.exec_command('\n')
stdin, stdout, stderr = ssh.exec_command(command3 , get_pty=True)


# Print the output
print(stdout.read().decode())


print("Script actions to transfer image file have started")
time.sleep(30)

# Close the SSH connection
ssh.close()

                                                  
