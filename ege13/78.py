import ipaddress

for m in range(15, 32):
    net = ipaddress.ip_network(f"61.58.73.42/{m}", 0)
    ip = ipaddress.ip_address("61.58.75.136")
    if ip in net:
        print(net, net.netmask)