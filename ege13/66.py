import ipaddress

for m in range(15, 32):
    net = ipaddress.ip_network(f"214.228.114.203/{m}", 0)
    print(net)