import itertools

a = set()
for i in itertools.permutations("ассасин", r = 7):
    s = ''.join(i)
    a.add(i)
    print(i)
print(len(a))
