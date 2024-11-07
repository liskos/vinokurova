import ipaddress

net = ipaddress.ip_network("240.248.252.0/255.255.252.0") # 240.248.252.0 - ip адрес, 255.255.252.0 - маска
ip1 = ipaddress.ip_address("240.248.254.248")
print(net)
for i in net:
    print(i.__format__("b"))