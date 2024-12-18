import ipaddress

for m in range(15, 32):
    net = ipaddress.ip_network(f"217.138.127.144/{m}", 0)
    print(net)