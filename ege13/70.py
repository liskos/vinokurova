import ipaddress

for m in range(15, 32):
    net = ipaddress.ip_network(f"115.127.30.120/{m}", 0)
    print(net)