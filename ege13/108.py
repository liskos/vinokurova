import ipaddress

for i in range(15, 32):
    net = ipaddress.ip_network(f"218.217.212.15/{i}", 0)
    print(net)

# 218.217.192.0/18
# 218.217.192.0/19
# Ответ 2
