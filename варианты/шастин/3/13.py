import ipaddress

for m in range(10, 30):
    net  = ipaddress.ip_network(f"205.154.212.0/{m}", 0)
    print(net, net.netmask)