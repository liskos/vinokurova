def f(n):
    b = bin(n)[2:]
    if n % 2 != 0:
        b = "1" + b + "0"
    elif n % 2 == 0:
        b = "11" + b + "11"
    return int(b, 2)


for i in range(1, 1000):
    if f(i) % 2 == 0 and f(i) < 126:
        print(f(i))
        