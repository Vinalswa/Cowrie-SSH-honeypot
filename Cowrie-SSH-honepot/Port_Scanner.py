import socket
import threading

target = input("Enter the target IP address: ")
ports = [21,22,23,25,53,80,110,139,143,443,445,3389]

print(f"\nScanning target: {target}\n")

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is OPEN")
        s.close()
    except:
        pass

threads = []
for port in ports:
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("\nScan complete ✅")
