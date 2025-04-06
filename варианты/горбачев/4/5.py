def p(n):
    s = ''
    while n> 0 :
        s = str(n%5) +s
        n = n//5
    return s

def f(n):
    r = p(n)
    if n % 2 == 0:
        r = "3" + r + str(n%5)
    else:
        r =str(n%4) + r + "4"
    return int(r, 5)

print(f(6), f(13))
a = set()
for i in range(1, 1000):
    if i <= 15:
        a.add(f(i))
print(max(a))
