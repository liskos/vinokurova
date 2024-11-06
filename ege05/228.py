def f(n):
    b = bin(n)[2:]
    b = str(b) + str(b[-2])
    b = str(b) +str(b[1])
    return int(b, 2)

print(f(11))
a = set()
for i in range(2, 10000):
    if f(i) <= 190:
        a.add(i)
print(max(a))