def f(n):
    b = bin(n)[2:]
    if n % 3 == 0:
        b = "101" + b[3:]
    else:
        b = "111" + b[3:]
    return int(b,2)

print(f(6), f(13))
for i in range(1, 35):
    if f(i) > 30:
        print(f(i))