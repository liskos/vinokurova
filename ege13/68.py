import ipaddress

for m in range(15, 32):
    net = ipaddress.ip_network(f"135.116.177.140/{m}", 0)
    print(net)