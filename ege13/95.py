import ipaddress

for m in range(10, 32):
    net = ipaddress.ip_network(f"241.185.253.57/{m}", 0)
    print(net)