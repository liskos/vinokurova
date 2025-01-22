import ipaddress

for m in range(10, 32):
    net = ipaddress.ip_network(f"133.57.64.130/{m}", 0)
    print(net)