def f(n):
    s1, s2, s3 = str(n)
    a1 = int(s1) * int(s2)
    a2 = int(s2) * int(s3)
    m = sorted([a1, a2])
    return str(m[1]) + str(m[0])


print(f(179))
for i in range(100, 1000):
    if f(i) == "123":
        print(i)
        break