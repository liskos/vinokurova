import ipaddress

for m in range(10, 32):
    net = ipaddress.ip_network(f"192.168.104.15/{m}", 0)
    print(net)