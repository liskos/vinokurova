import ipaddress

for m in range(10, 32):
    net = ipaddress.ip_network(f"116.123.64.53/{m}", 0)
    print(net)