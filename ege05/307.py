def f(n):
    n2 = bin(n - bin(n)[2:].count("0"))[2:]
    n2 = str(n2[-3:]) + n2
    return int(n2, 2)

print(f(13))
a = set()
for i in range(1, 1000):
    if f(i) > 224:
        a.add(f(i))
print(min(a))


