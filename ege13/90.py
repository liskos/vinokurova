import ipaddress

for m in range(10, 32):
    net = ipaddress.ip_network(f"163.232.136.60/{m}", 0)
    print(net)