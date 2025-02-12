import ipaddress

for i in range(10, 32):
    net = ipaddress.ip_network(f"200.154.190.12/{i}", 0)
    print(net, net.netmask)