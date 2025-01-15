import ipaddress

for m in range(10, 32):
    net = ipaddress.ip_network(f"221.117.97.115/{m}", 0)
    print(net)