import ipaddress

for m in range(10, 32):
    net = ipaddress.ip_network(f"159.152.66.19/{m}", 0)
    print(net)