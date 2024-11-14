def f(n):
    b = bin(n)[2:]
    if n % 2 != 0:
        b = "1" + b + "0"
    elif n % 2 == 0:
        b = "11" + b + "11"
    return int(b, 2)

a = set()
print(f(14))
for i in range(1, 1500):
    if f(i) < 126:
        a.add(f(i))
print(max(a))
        