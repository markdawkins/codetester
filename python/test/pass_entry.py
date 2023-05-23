import paramiko

# Read IP addresses from an external text file
def read_ip_list(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

ip_file_path = 'ip_list.txt'  # Specify the path to the text file containing IP addresses
ip_list = read_ip_list(ip_file_path)  # Read IP addresses from the file

username_list = ['user1', 'user2', 'user3']  # Replace with your list of usernames
password_list = ['pass1', 'pass2', 'pass3']  # Replace with your list of passwords

def login(ip, username, password):
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(ip, username=username, password=password, timeout=5)
        return True
    except paramiko.AuthenticationException:
        return False
    except Exception as e:
        print(f"Error connecting to {ip}: {e}")
    return False

def find_matching_credentials():
    for ip in ip_list:
        print(f"Trying to log in to {ip}...")
        for i in range(len(username_list)):
            if login(ip, username_list[i], password_list[i]):
                print(f"Successfully logged in to {ip} as {username_list[i]} with password {password_list[i]}")
                return

    print("No matching credentials found.")

find_matching_credentials()
