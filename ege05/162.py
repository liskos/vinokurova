def f(n):
    b = bin(n)[2:]
    b = b[::-1]
    b = b[b.find("1"):]
    return int(b, 2)

a = []
for i in range(1, 101):
    if f(i) == 9:
        a.append(i)
print(max(a))