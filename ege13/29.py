import ipaddress

net = ipaddress.ip_network("162.198.0.157/255.255.255.224",0)
ip = ipaddress.ip_address("162.198.0.157")
print(int(ip.__format__("b")[-5:],2))