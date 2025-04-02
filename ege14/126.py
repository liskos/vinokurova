def f(n):
    s = ""
    while n > 0:
        s = str(n%4) + s
        n = n // 4
    return s

for x in range(0, 1000):
    if str(hex(x))[-3] == "1" and str(hex(x))[-1] == "0" and str(oct(x))[-3] == "5" and str(oct(x))[-2] == "6":
        print(x)