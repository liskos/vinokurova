def f(n):
    b = bin(n)[2:]
    if n % 2 != 0:
        b = "1" + b + "11"
    else:
        b = "11" + b + "00"
    return int(b, 2)

a = set()
for i in range(1, 1000):
    if f(i) < 127:
        a.add(f(i))
print(max(a))