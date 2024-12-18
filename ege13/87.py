import ipaddress

for m in range(10, 32):
    net = ipaddress.ip_network(f"148.228.112.0/{m}", 0)
    print(net)