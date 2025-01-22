import ipaddress

for i in range(15, 32):
    net = ipaddress.ip_network(f"111.81.208.27/{i}", 0)
    ip = ipaddress.ip_address("111.81.192.0")
    if ip in net:
        print(net)
print(32-18, 2**14 )