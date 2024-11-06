def f(n):
    b = bin(n)[2:]
    b = b + str(sum(map(int, str(b))) % 2)
    b = b + str(sum(map(int, str(b))) % 2)
    return int(b, 2)

print(f(13))
for i in range(1, 10000):
    if f(i) > 100:
        print(f(i))
        break