def f(n):
    s = ""
    while n > 0:
        s = str(n%4) + s
        n = n // 4
    return s

for x in range(0, 1000):
    if str(hex(x))[-2] == "7" and str(oct(x))[-3] == "5" and str(oct(x))[-1] == "6" and f(x)[-2] == "1":
        print(x)