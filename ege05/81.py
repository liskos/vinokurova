def f(n):
    s1, s2, s3, s4 = str(n)
    a1 = int(s1) + int(s4)
    a2 = int(s2) + int(s3)
    m = sorted([a1, a2])
    return str(m[1]) + str(m[0])



for i in range(1000, 10000):
    if f(i) == "128":
        print(i)
        break
