a = 8**1023 + 2**1024 - 3
b = bin(a)[2:]
print(b.count("1"))