import ipaddress
from ipaddress import ip_network

for m in range(10, 32):
    net = ipaddress.ip_network(f"111.81.208.27/{m}", 0)
    ip = ipaddress.ip_address("111.81.192.0")
    if ip in net:
        print(net, net.netmask)