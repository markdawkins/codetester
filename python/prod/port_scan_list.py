
####Still work to be done on this script. Need to change input port 4876 to be a variable so that it does not have to be manually 
##changed in script code.
import nmap
#port_number = input('enter port number: ')

def port_scan(ip):
    nm = nmap.PortScanner()
    #nm.scan(ip, port_number, arguments='-Pn')
    nm.scan(ip, '4876', arguments='-Pn')      ###Change the port number to scanned here in this exampe we are using tcp port 4876
    return nm[ip]['tcp'][4876]['state']         ###Change the port number to scanned here in this exampe we are using tcp port 4876

def main():
    ip_file = './LISTS/'+ filename + '.txt'  # Replace with the path to your IP addresses text file

    with open(ip_file, 'r') as file:
        ip_list = file.read().splitlines()

    for ip in ip_list:
        result = port_scan(ip)
        print(f"Scan result for {ip}: {result}")

if __name__ == '__main__':
    main()
