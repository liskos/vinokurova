import ipaddress

for m in range(10, 32):
    net = ipaddress.ip_network(f"76.155.48.2/{m}", 0)
    print(net)