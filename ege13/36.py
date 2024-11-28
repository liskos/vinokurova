import ipaddress

net = ipaddress.ip_network("132.126.150.18/255.255.240.0", 0)
ip = ipaddress.ip_address("132.126.150.18")
print(int(ip.__format__("b")[-5:], 2))