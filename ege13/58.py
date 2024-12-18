import ipaddress

for m in range(15, 32):
    net = ipaddress.ip_network(f"134.92.108.145/{m}", 0)
    print(net)