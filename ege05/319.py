def f(n):
    b = bin(n)[2:]
    if n % 10 == 0:
        b = b + b[-4:]
    else:
        b = b + str(bin(((n%10)**2)//2)[2:])
    return int(b, 2)

print(f(20))
a = 0
for i in range(11, 1000):
    if f(i) < 680:
        a += 1
        print(i)
print(a)

