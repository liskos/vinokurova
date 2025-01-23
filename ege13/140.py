import ipaddress

for m in range(10, 32):
    net1 = ipaddress.ip_network(f"112.166.78.114/{m}", 0)
    net2 = ipaddress.ip_network(f"112.166.78.117/{m}", 0)
    ip1 = ipaddress.ip_address("112.166.78.114")
    ip2 = ipaddress.ip_address("112.166.78.117")
    if ip1 not in net2 and ip2 not in net1:
        if ip1 != net1[0] and ip2 != net2[-1]:
            print(net1, net2)