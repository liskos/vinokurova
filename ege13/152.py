import ipaddress

for i in range(10,32):
    net = ipaddress.ip_network(f"111.3.161.27/{i}", 0)
    print(net, net.netmask, 2**(32-i))