def f(n):
    t = str(n)
    x, y, z = t
    a = [x+y, x+z, y+x, y+z, z+x, z+y]
    a = [int(s) for s in a if s[0] != "0"]
    return int(max(a)) - int(min(a))


print(f(351))
s = set()
for i in range(100, 1000):
    if f(i) == 50:
        s.add(i)
print(max(s))