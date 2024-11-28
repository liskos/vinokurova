import ipaddress

net = ipaddress.ip_network("122.191.12.189/255.255.255.128", 0)
ip = ipaddress.ip_address("122.191.12.189")
print(int(ip.__format__("b")[-5:], 2))