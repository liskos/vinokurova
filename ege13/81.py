import ipaddress

for m in range(10, 32):
    net = ipaddress.ip_network(f"215.181.200.27/{m}", 0)
    print(net, net.netmask)