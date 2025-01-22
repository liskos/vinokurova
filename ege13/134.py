import ipaddress

for i in range(10, 32):
    net = ipaddress.ip_network(f"121.171.15.149/{i}", 0)
    ip = ipaddress.ip_address("121.171.15.143")
    if ip in net:
        print(net)
print(2**(32-27))