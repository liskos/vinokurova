import ipaddress

for m in range(10, 32):
    net = ipaddress.ip_network(f"138.75.241.160/{m}", 0)
    print(net)