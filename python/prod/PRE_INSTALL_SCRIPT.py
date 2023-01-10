import time
#DEFINE VARIABLES
#ALL COMMANDS BELOW NEED TO BE RUN FROM CONSOLE USING SERIAL COMMANDS
DEVICE_NAME = input('Enter Hostname:')
VLAN10_IP = input('Enter VLAN 10 IP:')
ROUTER_IP = input('Enter Router IP:')
STREET_ADDRESS = input('Enter Street address:')

net_connect.send_command('config t\n')
net_connect.send_command('username admin privilege 15 secret barrier1\n')
net_connect.send_command('username solar privilege 15 password Ts&SQLt$')
net_connect.send_command('snmp-server community L0$alim0$-RO RO')
net_connect.send_command('enable secret barrier1\n')
net_connect.send_command('snmp-server user M1bAcc355 ALLADMIN v3 auth md5 D0uHv3M1lK!\n')
net_connect.send_command('line vty 0 4\n')
net_connect.send_command('transport input all\n')
net_connect.send_command('login local')
net_connect.send_command('interface GigabitEthernet0/0\n')
net_connect.send_command('ip address dhcp\n')
net_connect.send_command('no shut\n')
net_connect.send_command('end\n')
net_connect.send_command('wr mem\n')
net_connect.send_command('exit\n')
print ("Configuration saved to device...")
time.sleep(1)