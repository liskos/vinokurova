def f(n):
    b = hex(n//2)[2:]
    if n % 4 != 0:
        b = "f" + b + "a0"
    else:
        b = "15" + b + "c"
    return int(b, 16)


for i in range(1, 1000):
    if f(i) < 65536:
        print(i)