import ipaddress

for i in range(10,32):
    net = ipaddress.ip_network(f"115.53.128.88/{i}", 0)
    print(net, net.netmask)