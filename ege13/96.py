import ipaddress

for m in range(10, 32):
    net = ipaddress.ip_network(f"204.108.112.142/{m}", 0)
    print(net)