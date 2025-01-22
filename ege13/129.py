import ipaddress

for i in range(15, 32):
    net = ipaddress.ip_network(f"108.133.75.91/{i}", 0)
    ip = ipaddress.ip_address("108.133.75.64")
    if ip in net:
        print(net)
print(2**(32-27))