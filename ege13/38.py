import ipaddress

net = ipaddress.ip_network("126.185.90.162/255.255.252.0", 0)
ip = ipaddress.ip_address("126.185.90.162")
print(int(ip.__format__("b")[-5:], 2))