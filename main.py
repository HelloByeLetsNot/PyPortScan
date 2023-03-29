import socket

# Define a function to scan a website for open ports and write the results to a file
def scan_ports(hostname, output_file):
    print(f"Scanning ports for {hostname}...")
    # Define a list of ports to scan
    ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 465, 587, 993, 995]
    with open(output_file, "w") as f:
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((hostname, port))
            if result == 0:
                print(f"Port {port} is open")
                f.write(f"Port {port} is open\n")
            sock.close()
        print("Port scan complete")
        f.write("Port scan complete\n")

# Call the function with a website to scan and a filename for the output
scan_ports("www.example.com", "results.txt")
