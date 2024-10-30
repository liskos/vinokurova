def s(n):
    ss = 0
    for i in range(1, int(n ** 0.5)+ 1):
        if n % i == 0:
            if i != n // i:
                ss += i
                ss += n// i
            else:
                ss += i
    return ss


for i in range(1000, 10000):
    if s(i) % 100 == 23:
        print(i, s(i))