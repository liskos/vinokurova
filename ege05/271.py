def sh(n):
    s = ""
    while n > 0:
        s = str(n % 4) + s
        n = n // 4
    return s


def f(n):
    b = bin(n)[2:]
    if n % 2 != 0:
        b = "2" + b + "11"
    else:
        b = "13" + b + "02"
    return int(b, 4)


for i in range(1, 1000):
    if f(i) > 1000:
        print(f(i))
        break