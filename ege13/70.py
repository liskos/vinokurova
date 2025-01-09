import ipaddress

for m in range(10, 32):
    net = ipaddress.ip_network(f"115.127.30.120/{m}", 0)
    ip = ipaddress.ip_address("115.127.151.120")
    if ip in net:
        print(net, net.netmask)