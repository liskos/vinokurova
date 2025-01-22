import ipaddress

for m in range(10, 32):
    net = ipaddress.ip_network(f"154.112.144.160/{m}", 0)
    print(net)