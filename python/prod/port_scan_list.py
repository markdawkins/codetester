import nmap
port_number = input('enter port number: ')

def port_scan(ip):
    nm = nmap.PortScanner()
    nm.scan(ip, port_number, arguments='-Pn')
    return nm[ip]['tcp'][4876]['state']

def main():
    ip_file = './LISTS/vstack_2.txt'  # Replace with the path to your IP addresses text file

    with open(ip_file, 'r') as file:
        ip_list = file.read().splitlines()

    for ip in ip_list:
        result = port_scan(ip)
        print(f"Scan result for {ip}: {result}")

if __name__ == '__main__':
    main()
