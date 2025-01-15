import ipaddress

for m in range(10, 32):
    net = ipaddress.ip_network(f"193.138.70.47/{m}", 0)
    print(net)