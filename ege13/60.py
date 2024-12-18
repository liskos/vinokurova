import ipaddress

for m in range(15, 32):
    net = ipaddress.ip_network(f"145.192.186.230/{m}", 0)
    print(net)