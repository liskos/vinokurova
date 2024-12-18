import itertools

a = set()
for i in itertools.permutations("молоко", r = 6):
    s = ''.join(i)
    a.add(i)
    print(i)
print(len(a))
