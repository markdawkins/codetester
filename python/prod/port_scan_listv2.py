import socket

def scan_port(ip, port, protocol):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM if protocol == 'tcp' else socket.SOCK_DGRAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} ({protocol.upper()}) is open on {ip}")
        sock.close()
    except Exception as e:
        print(f"Error while scanning {ip}: {e}")

def main():
    try:
        list = input("Enter the name of the IP list file (e.g., ip_list): ")
        list_name = "../lists/%s.txt" % list
        protocol = input("Enter 'tcp' or 'udp' for port scanning protocol: ")
        start_port = int(input("Enter the starting port number: "))
        end_port = int(input("Enter the ending port number: "))

        with open(list_name, "r") as file:
            ip_list = file.read().splitlines()

        for ip in ip_list:
            for port in range(start_port, end_port + 1):
                scan_port(ip, port, protocol)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
