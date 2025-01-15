import ipaddress

for m in range(10, 32):
    net = ipaddress.ip_network(f"208.207.230.65/{m}", 0)
    print(net)