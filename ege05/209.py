def f(n):
    b = bin(n)[2:]
    b = b + str(sum(map(int, str(b))) % 2)
    b = b + str(sum(map(int, str(b))) % 2)
    return int(b, 2)

print(f(13))
a = []
for i in range(1, 1000):
    if 90 <= f(i) <= 160:
        a. append(f(i))
print(a, len(a))