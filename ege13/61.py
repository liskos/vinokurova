import ipaddress

for m in range(15, 32):
    net = ipaddress.ip_network(f"158.198.104.220/{m}", 0)
    print(net)