def f(n):
    b = bin(n)[2:]
    if n % 2 == 0:
        b = "10" + b + "1"
    else:
        b = "1" + b + "01"
    return int(b, 2)

print(f(13))
a = set()
for i in range(1, 1000):
    if f(i) > 420:
        a.add(i)
print(min(a))
