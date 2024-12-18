import itertools

a = set()
for i in itertools.permutations("тратата", r = 7):
    s = ''.join(i)
    a.add(i)
    print(i)
print(len(a))
