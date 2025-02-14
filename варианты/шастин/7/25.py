import fnmatch

def d(n):
    a = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return a

def mask(a):
    for i in sorted(a):
        if fnmatch.fnmatch(str(i), "2*3?"):
            return True, i
    return False, 0

k = 0
for i in range(500001, 10**10):
    if mask(d(i))[0]:
        k += 1
        print(i, mask(d(i))[1])
        if k == 5:
            break

