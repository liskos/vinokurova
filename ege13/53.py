import ipaddress

for m in range(15, 32):
    net = ipaddress.ip_network(f"220.128.112.142/{m}", 0)
    print(net)