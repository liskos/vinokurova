def f(n):
    s1, s2, s3 = str(n)
    a1 = int(s1) + 3
    a2 = int(s2) + 6
    a3 = int(s3) + 5
    return str(min(a1, a2, a3)) + str(a1 + a2 + a3 - max(a1, a2, a3) - min(a1, a2, a3)) + str(max(a1, a2, a3))


for i in range(100, 1000):
    if f(i) == "51014":
        print(i)
