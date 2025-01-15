import ipaddress

for m in range(10, 32):
    net = ipaddress.ip_network(f"192.75.64.98/{m}", 0)
    print(net)