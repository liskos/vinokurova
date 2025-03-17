def prime_numbers(n):
    a = [True] * n
    a[0] = a[1] = False
    for i in range(n):
        if a[i]:
            for j in range(i**2, n, i):
                a[j] = False
    b = [i for i in range(n) if a[i]]
    return b

p = prime_numbers(3000000)
k = 0
for i in range(3333337+1, 10**10):
    a = []
    for j in p:
        if i%j == 0 and i != j:
            a.append(j)
    r = max(a) - min(a)
    if r > 1000 and r %3 == 0:
        print(i, r)
        k += 1
        if k == 5:
            break
