import ipaddress

for m in range(10, 32):
    net = ipaddress.ip_network(f"18.168.250.32/{m}", 0)
    print(net)