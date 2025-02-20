def f(s):
    while "25" in s or "355" in s or "555" in s:
        if "25" in s:
            s = s.replace("25", "5", 1)
        if "355" in s:
            s = s.replace("355", "522", 1)
        if "555" in s:
            s = s.replace("555", "3", 1)
    return s

for n in range(3, 10000+1):
    s = "2" + "5" * n
    if f(s).count("2") == 10:
        print(n)
        break
