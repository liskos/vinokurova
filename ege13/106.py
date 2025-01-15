import ipaddress

for m in range(10, 32):
    net = ipaddress.ip_network(f"212.168.104.5/{m}", 0)
    print(net)