import ipaddress

for m in range(10, 32):
    net = ipaddress.ip_network(f"149.112.71.192/{m}", 0)
    print(net)