import ipaddress

net = ipaddress.ip_network("156.128.0.227/255.255.255.248", 0)
ip = ipaddress.ip_address("156.128.0.227")
print(int(ip.__format__("b")[-5:],2))