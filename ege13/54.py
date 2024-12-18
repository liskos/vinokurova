import ipaddress

for m in range(15, 32):
    net = ipaddress.ip_network(f"148.228.120.242/{m}", 0)
    print(net)