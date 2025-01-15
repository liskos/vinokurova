import ipaddress

for m in range(15, 32):
    net = ipaddress.ip_network(f"215.171.155.54/{m}", 0)
    ip = ipaddress.ip_address("215.171.145.37")
    if ip in net:
        print(net, net.netmask)