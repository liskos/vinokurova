import ipaddress

for m in range(10, 32):
    net = ipaddress.ip_network(f"48.95.137.38/{m}", 0)
    print(net)