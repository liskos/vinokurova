import ipaddress

for m in range(10, 32):
    net = ipaddress.ip_network(f"203.155.64.98/{m}", 0)
    print(net)