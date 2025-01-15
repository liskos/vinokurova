import ipaddress

for m in range(15, 32):
    net = ipaddress.ip_network(f"121.171.5.70/{m}", 0)
    ip = ipaddress.ip_address("121.171.29.68")
    if ip in net:
        print(net, net.netmask)