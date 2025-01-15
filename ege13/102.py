import ipaddress

for m in range(10, 32):
    net = ipaddress.ip_network(f"120.120.120.35/{m}", 0)
    print(net)