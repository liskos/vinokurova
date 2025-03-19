def f(s):
    while "=3" in s or "=4" in s or "=5" in s:
        if "=3" in s:
            s = s.replace("=3", "55=")
        if "=4" in s:
            s = s.replace("=4", "4=")
        if "=5" in s:
            s = s.replace("=5", "3=")
    return s

for n in range(1, 10000):
    s = "=" + "3" * 51 + "4" * n + "5"* 53
