import ipaddress
a = 0
net = ipaddress.ip_network("232.116.0.0/255.255.240.0", 0)
for ip in net:
    if bin(int(ip))[2:].count("1") % 4 == 0:
        a += 1
        print(ip)
print(a)