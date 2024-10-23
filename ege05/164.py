a = []
for n in range(1, 501):
    b = bin(n)[2:]
    b = b[::-1]
    b = b[b.find("1"):]
    if int(b, 2) == 13:
        a.append(n)
print(max(a))
