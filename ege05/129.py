def f(n):
    s1, s2, s3, s4 = str(n)
    a1 = int(s1) + int(s2)
    a2 = int(s2) + int(s3)
    a3 = int(s3) + int(s4)
    m = sorted([a1,a2,a3])
    return str(m[1]) + str(m[0])

print(f(1284))
for i in range(1000, 10000):
    if f(i) == '145':
        print(i)