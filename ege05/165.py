a = []
for i in range(1, 1001):
    b = bin(i)[2:]
    b = b[::-1]
    b =b[b.find("1"):]
    if int(b, 2) == 23:
        a.append(i)
print(max(a))