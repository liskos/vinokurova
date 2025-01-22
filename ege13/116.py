import ipaddress

for m in range(10, 32):
    net = ipaddress.ip_network(f"151.181.88.129/{m}", 0)
    print(net)