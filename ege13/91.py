import ipaddress

for m in range(10, 32):
    net = ipaddress.ip_network(f"108.87.113.106/{m}", 0)
    print(net)