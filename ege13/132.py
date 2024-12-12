import ipaddress

for i in range(15, 32):
    net = ipaddress.ip_network(f"112.117.107.70/{i}", 0)
    ip = ipaddress.ip_address("112.117.121.80")
    if ip in net:
        print(net)
print(32-19, 2**13)