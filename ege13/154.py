import ipaddress

for i in range(10, 32):
    net = ipaddress.ip_network(f"125.28.160.73/{i}", 0)
    print(net, net.netmask, 2**(32-i))
    