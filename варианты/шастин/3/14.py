def pt(n):
    s = ""
    while n > 0:
        s = str(n % 5) + s
        n = n // 5
    return s

for x in range(1, 5556):
    s = 5 ** 150 + 5** 135 - x
    if pt(s).count("4") == 134:
        print(x)