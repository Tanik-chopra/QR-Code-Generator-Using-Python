
import socket
def scan_ports(target, ports):
    open_ports = []
    
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        
        if result == 0:
            open_ports.append(port)
        
        sock.close()
    
    return open_ports

def main():
    target = input("Enter the IP address or URL: ")
    scan_option = input("Choose scan option:\n1. Specific Ports\n2. Port Range\nEnter your choice: ")
    
    if scan_option == '1':
        ports = input("Enter the specific ports (comma-separated): ")
        ports = [int(p.strip()) for p in ports.split(',')]
    elif scan_option == '2':
        start_port = int(input("Enter start port: "))
        end_port = int(input("Enter end port: "))
        ports = range(start_port, end_port + 1)
    else:
        print("Invalid choice.")
        return
    
    print(f"Scanning {target} for open ports...")
    
    open_ports = scan_ports(target, ports)
    
    if open_ports:
        print("Open ports:")
        for port in open_ports:
            print(f"Port {port} is open")
    else:
        print("No open ports found.")

if __name__ == "__main__":
   main()

#With this version of the script, after entering the IP address or URL, the user can choose between scanning specific ports (option 1) or a port range (option 2). Depending on the chosen option, the user will be prompted to input either specific port numbers (comma-separated) or a start and end port for the range. The script will then proceed to scan the specified ports or range and display the open ports.