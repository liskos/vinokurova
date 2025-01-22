import ipaddress

for m in range(10, 32):
    net = ipaddress.ip_network(f"194.162.77.94/{m}", 0)
    print(net)