import paramiko
import time
from getpass import getpass 

password = getpass()
passwd = password

# List of cisco AP IP addresses
LIST = input("Enter List Name:")
listname  = "\LISTS\%s.txt"  % LIST



f = open (listname)
    # Connect to each AP on list
for ip in f:
        device = ip.strip()


        #ap_ip = input('Enter AP IP: ')

        def connect(server_ip, server_port, user, passwd):
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            print(f'Connecting to {server_ip}')
            ssh_client.connect(hostname=server_ip, port=server_port, username=user, password=passwd,
                            look_for_keys=False, allow_agent=False)
            return ssh_client

        def get_shell(ssh_client):
            shell = ssh_client.invoke_shell()
            return shell

        def send_command(shell, command, timout=1):
            print(f'Sending command: {command}')
            shell.send(command + '\n')
            time.sleep(timout)

        def show(shell, n=10000):
            output = shell.recv(n)
            return output.decode()

        def close(ssh_client):
            if ssh_client.get_transport().is_active() == True:
                print('Closing connection')
                ssh_client.close()

        if __name__ == '__main__':
            router1 = {'server_ip': device , 'server_port': '22', 'user':'admin', 'passwd': passwd}
            client = connect(**router1)
            shell = get_shell(client)
            time.sleep(3)
            send_command(shell, 'enable')
            time.sleep(3)
            send_command(shell, passwd) # this is the enable password
            send_command(shell, 'term len 0')
            send_command(shell, 'archive download-sw /no-reload sftp://172.168.2.167/ap3g3')
            time.sleep(10)
            send_command(shell, 'apdl')
            send_command(shell, 'gEQAAp3C')
            time.sleep(120)
            output = show(shell)
            print(output)



