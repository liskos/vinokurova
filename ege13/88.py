import ipaddress

for m in range(10, 32):
    net = ipaddress.ip_network(f"63.132.140.28/{m}", 0)
    print(net)