def f(n):
    s = ""
    while n > 0:
        s = str(n%4) + s
        n = n // 4
    return s

for x in range(0, 1000):
    if str(hex(x))[-2] == "e" and str(oct(x))[-2] == "5" and str(bin(x))[-3] == "1" and f(x)[-1] == "1":
        print(x)