def f(n):
    s1, s2, s3, s4 = str(n)
    a1 = int(s1) + int(s2)
    a2 = int(s3) + int(s4)
    m = sorted([a1, a2])
    return str(m[0]) + str(m[1])



print(f(3165))
for i in range(1000, 10000):
    if f(i) == "912":
       print(i)
