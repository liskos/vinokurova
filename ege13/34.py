import ipaddress

net = ipaddress.ip_network("156.132.15.138/255.255.252.0", 0)
ip = ipaddress.ip_address("156.132.15.138")
print(int(ip.__format__("b")[-5:], 2))