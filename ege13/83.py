import ipaddress

for m in range(10, 32):
    net = ipaddress.ip_network(f"115.12.69.38/{m}", 0)
    print(net, net.netmask)