import ipaddress
net = ipaddress.ip_network("123.222.111.192/255.255.255.248")
for ip in net:
    if ip.packed[3].__format__("b").count("0") % 3 != 0:
        print(ip)