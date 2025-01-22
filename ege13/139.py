import ipaddress

for m in range(10, 32):
    net1 = ipaddress.ip_network(f"132.46.175.26/{m}", 0)
    net2 = ipaddress.ip_network(f"132.46.170.130/{m}", 0)
    ip1 = ipaddress.ip_address("132.46.175.26")
    ip2 = ipaddress.ip_address("132.46.170.130")
    if ip1 not in net2 and ip2 not in net1:
        if ip1 != net1[-1] and ip2 != net2[0]:
            print(net1, net2)