import ipaddress

net = ipaddress.ip_network("/255.255.255.128.", 0)
print(len(list(net))- 2)