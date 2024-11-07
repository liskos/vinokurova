import ipaddress

net = ipaddress.ip_network("119.119.28.128/255.255.254.0", 0)
print(len(list(net))- 2)