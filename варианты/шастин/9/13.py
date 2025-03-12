import ipaddress

for m in range(10, 32):
    net = ipaddress.ip_network(f"111.233.75.16/{m}", 0)
    ip = ipaddress.ip_address("111.233.75.0")
    if ip in net:
        print(net, net.netmask)