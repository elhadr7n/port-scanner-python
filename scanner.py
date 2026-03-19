import socket
target = input("Enter target IP or domain: ")
print(f"\nScanning common ports on {target}...\n")

common_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445]

for port in common_ports:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(1)

	result = s.connect_ex((target, port))
	if result == 0:
	   print(f"Port {port} is OPEN")
	   
	s.close()
print("\nScan finished.")