import ipaddress

for i in range(10, 32):
    net1 = ipaddress.ip_network(f"200.154.190.12/{i}", 0)
    net2 = ipaddress.ip_network(f'200.154.184.0/{i}', 0)
    ip1 = ipaddress.ip_address("200.154.190.12")
    ip2 = ipaddress.ip_address("200.154.184.0")
    if ip1 in net2 and ip2 in net1:
        print(net1, net2)