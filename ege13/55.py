import ipaddress

for m in range(15, 32):
    net = ipaddress.ip_network(f"248.228.60.240/{m}", 0)
    print(net)