import ipaddress

for i in range(15, 32):
    net = ipaddress.ip_network(f"156.133.216.0/{i}", 0)
    ip = ipaddress.ip_address("156.133.216.35")
    if ip in net:
        print(net)
print(2**(32-21))