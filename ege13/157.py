import ipaddress

for i in range(10,32):
    net = ipaddress.ip_network("192.168.248.176/255.255.255.240")
    print(net)