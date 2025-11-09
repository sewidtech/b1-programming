

devices = [ ("192.168.1.10", [22, 80, 443]),
("192.168.1.11", [21, 22, 80]), ("192.168.1.12", [23,
80, 3389])]

risky_ports = [21, 23, 3389]

for ip , open_ports in devices :
    for port in open_ports :
        if port in risky_ports:
            print("WARNING:"),  print(f"{ip} has risky {port} open")



print ("scan complete")