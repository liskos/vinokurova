import ipaddress
from ipaddress import ip_address

for m in range(10, 32):
    net = ipaddress.ip_network(f"154.28.80.25/{m}", 0)
    ip = ipaddress.ip_address("154.28.90.25")
    if ip in net:
        print(net, net.netmask)