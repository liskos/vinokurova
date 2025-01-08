import ipaddress

for m in range(15, 32):
    net = ipaddress.ip_network(f"152.217.69.70/{m}", 0)
    print(net)