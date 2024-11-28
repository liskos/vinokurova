import ipaddress

net = ipaddress.ip_network("206.158.124.67/255.255.240.0", 0)
ip = ipaddress.ip_address("206.158.124.67")
print(int(ip.__format__("b")[-5:], 2))