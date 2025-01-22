import ipaddress

for m in range(10, 32):
    net = ipaddress.ip_network(f"106.113.64.105/{m}", 0)
    print(net)