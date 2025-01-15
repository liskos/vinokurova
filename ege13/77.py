import ipaddress

for m in range(15, 32):
    net = ipaddress.ip_network(f"11.156.152.142/{m}", 0)
    ip = ipaddress.ip_address("11.156.157.39")
    if ip in net:
        print(net, net.netmask)