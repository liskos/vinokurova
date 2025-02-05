import ipaddress
from ipaddress import ip_address

for i in range(1, 32):
    net = ipaddress.ip_network("222.212.128.0/255.255.224.0")
    print(ipaddress)