import ipaddress

for m in range(10, 32):
    net = ipaddress.ip_network(f"214.224.120.40/{m}", 0)
    print(net)