import ipaddress

for m in range(10, 32):
    net = ipaddress.ip_network(f"125.181.67.15/{m}", 0)
    print(net)