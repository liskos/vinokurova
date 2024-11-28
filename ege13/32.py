import ipaddress

net = ipaddress.ip_network("10.18.134.220/255.255.255.192", 0)
ip = ipaddress.ip_address("10.18.134.220")
print(int(ip.__format__("b")[-5:], 2))