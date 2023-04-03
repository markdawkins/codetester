#paramkio_file
import paramiko
import time
import getpass
ssh_client =paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)

password = getpass.getpass('Enter password:')

router = {'hostname': '192.168.1.158' , 'port': '22' , 'username':'ansible:' , 'password': password}
print(f'Connecting to {router["hostname"]}')
ssh_client.connect(**router, look_for_keys=False , allow_agent=False)

shell = ssh_client.invoke_shell()
shell.send('terminal lenght 0\n')
shell.send('show version\n')
shell.send('show ip int brief\n')
time.sleep(1)

if ssh_client.get_transport().is_active()==True:
   print('Closing connection') 
   ssh_client.close()