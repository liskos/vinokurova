import ipaddress

for m in range(15,32 ):
    net = ipaddress.ip_network(f"222.190.122.24/{m}", 0)
    print(net)
print(2 **(32-21)-3)