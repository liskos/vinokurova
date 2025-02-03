def f(n):
    a = set()
    for i in range(2, int(n ** 0.5)+ 1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    a.add(1)
    return a

def f2(n):
    d = f(n)
    return sum(d)//len(d)

k = 0
for i in reversed(range(1, 770000)):
    if f2(i) % 100 == 12:
        print(i, f2(i))
        k += 1
        if k == 5:
            break