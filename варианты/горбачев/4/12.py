def f(s):
    while "96" in s or "366" in s or "666" in s:
        if "96" in s:
            s = s.replace("96", "6", 1)
        if "366" in s:
            s = s.replace("366", "69", 1)
        if "666" in s:
            s = s.replace("666", "3", 1)
    return s

a = set()
for n in range(4, 100):
    s = "9" + n*"6"
    r = f(s)
    a.add(sum(map(int, r)))
print(max(a))
