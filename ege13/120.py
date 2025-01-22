import ipaddress

for m in range(10, 32):
    net = ipaddress.ip_network(f"199.92.65.189/{m}", 0)
    print(net)