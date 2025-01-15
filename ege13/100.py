import ipaddress

for m in range(10, 32):
    net = ipaddress.ip_network(f"215.118.70.47/{m}", 0)
    print(net)