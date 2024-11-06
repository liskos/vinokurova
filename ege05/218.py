def f(n):
    t = str(n)
    x, y, z = t
    a = [x+y, x+z, y+x, y+z, z+x, z+y]
    a = [int(s) for s in a if s[0] != "0"]
    return int(max(a)) - int(min(a))


print(f(351))
k = 0
for i in range(300, 401):
    if f(i) == 20:
        k +=1
        print(i)
print(k)
