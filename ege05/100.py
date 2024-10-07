def f(n):
    s1, s2, s3, s4, s5 = str(n)
    a1 = int(s1) + int(s3) + int(s5)
    a2 = int(s2) + int(s4)
    m = sorted([a1,a2])
    return str(m[0]) + str(m[1])

print(f(63179))
for i in range(10000, 100000):
    if f(i) == '723':
        print(i)
        break