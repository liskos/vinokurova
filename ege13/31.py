import ipaddress

net = ipaddress.ip_network("192.168.156.235/255.255.255.240", 0)
ip = ipaddress.ip_address("192.168.156.235")
print(int(ip.__format__("b")[-5:], 2))