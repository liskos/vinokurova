import ipaddress

for m in range(15, 32):
    net = ipaddress.ip_network(f"161.158.136.231/{m}", 0)
    ip = ipaddress.ip_address("161.158.138.65")
    if ip in net:
        print(net, net.netmask)