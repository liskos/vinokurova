import ipaddress

for m in range(15, 32):
    net = ipaddress.ip_network(f"152.217.69.70/{m}", 0)
    ip = ipaddress.ip_address("152.217.125.80")
    if ip in net:
        print(net, net.netmask)