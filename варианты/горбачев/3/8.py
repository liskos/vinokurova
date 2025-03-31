import itertools

k = 0
for a in itertools.product(range(16), repeat = 5):
    if a[0] != 0 and a[0] % 2 == 0 and a[-1] % 2 == 1 and a[0] != a[1] != a[2] != a[3] != a[4]:
        k += 1
print(k)