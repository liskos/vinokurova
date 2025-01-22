import ipaddress

for m in range(10, 32):
    net = ipaddress.ip_network(f"131.149.64.13/{m}", 0)
    print(net)