import ipaddress

for i in range(10, 32):
    net = ipaddress.ip_network(f"175.122.80.13/{i}", 0)
    print(net, net.netmask, 2 ** (32 - i))
