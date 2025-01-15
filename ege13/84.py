import ipaddress

for m in range(10, 32):
    net = ipaddress.ip_network(f"68.112.69.138/{m}", 0)
    print(net)