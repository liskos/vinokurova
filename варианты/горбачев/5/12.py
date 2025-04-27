def f(s):
    while "700" in s or "100" in s or "000" in s:
        if "700" in s:
            s = s.replace("700", "01", 1)
        if "100" in s:
            s = s.replace("100", "07", 1)
        if "000" in s:
            s = s.replace("000", "1", 1)
    return s

a = set()
for n in range(1, 1000):
    s = "7" + n*"0"
    if f(s).count("7") == 7:
        a.add(n)
print(sum(a))