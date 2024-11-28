def f(n):
    b = bin(n)[2:]
    s = sum(map(int, str(b)))
    if s % 2 == 0:
        b = "10" + b[2:] + "0"
    else:
        b = "11" + b[2:] + "1"
    return int(b, 2)

print(f(4))
a = set()
for i in range(1, 1000):
    if f(i) >= 16:
        a.add(i)
print(min(a))

