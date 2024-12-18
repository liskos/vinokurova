import ipaddress

for m in range(15, 32):
    net = ipaddress.ip_network(f"117.191.88.37/{m}", 0)
    print(net)