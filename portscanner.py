import socket
import threading

def get_service_name(port):
    commonly_used_ports = {
        20: "FTP Data Transfer",
        21: "FTP Control",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        143: "IMAP",
        443: "HTTPS",
        3306: "MySQL",
        3389: "RDP",
        5432: "PostgreSQL",
        8080: "HTTP Alternate",
    }
    try:
        return socket.getservbyport(port)
    except:
        return commonly_used_ports.get(port, "Uknown Service")

def scan_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)  # Set a timeout for the connection attempt
        result = s.connect_ex((ip, port))
        if result == 0:
            service = get_service_name(port)
            print(f"\nPort {port} is open ({service})\n")
        s.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")
    
# Ask user to define target and range of ports to scan
target_ip = input("Enter the target IP address or hostname: ").strip()
port_start = int(input("Enter the starting port number: "))
port_end = int(input("Enter the ending port number: "))

print(f"\nScanning {target_ip} from port {port_start} to {port_end}...\n")
    
# Launch threads for each port in the specified range
threads = []
for port in range(port_start, port_end +1):
    t = threading.Thread(target=scan_port, args=(target_ip, port,))
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

print("\nPort scan completed.")