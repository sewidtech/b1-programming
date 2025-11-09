

print("Scanning network devices...")

devices = [
    ("192.168.1.10", [22, 80, 443]),
    ("192.168.1.11", [21, 22, 80]),
    ("192.168.1.12", [23, 80, 3389])
]

risky_ports = [21, 23, 3389]


found = {}

for ip, open_ports in devices:
    for port in open_ports:
        if port in risky_ports:
            
            # Get the value for ip if it exists — otherwise, give me an empty list ([]).”
            found[ip] = found.get(ip, []) + [port]
            print(f"WARNING: {ip} has risky port {port} open")

print("Scan complete")
