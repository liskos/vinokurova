import ipaddress

for m in range(15, 32):
    net = ipaddress.ip_network(f"153.209.31.240/{m}", 0)
    print(net)