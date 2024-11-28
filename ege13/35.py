import ipaddress

net = ipaddress.ip_network("112.154.133.208/255.255.248.0", 0)
ip = ipaddress.ip_address("112.154.133.208")
print(int(ip.__format__("b")[-5:], 2))