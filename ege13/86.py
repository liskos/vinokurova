import ipaddress

for m in range(10, 32):
    net = ipaddress.ip_network(f"156.32.140.138/{m}", 0)
    print(net)