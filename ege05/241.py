def f(n):
    b = bin(n)[2:].zfill(8)
    b2 = b[::-1]
    return int(b, 2) - int(b2, 2)

a = set()
for i in range(1, 256):
    a.add(f(i))
print(max(a))