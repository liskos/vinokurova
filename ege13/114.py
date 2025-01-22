import ipaddress

for m in range(10, 32):
    net = ipaddress.ip_network(f"132.47.160.46/{m}", 0)
    print(net)