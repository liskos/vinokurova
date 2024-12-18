import itertools

a = set()
for i in itertools.permutations("ворон", r = 5):
    s = ''.join(i)
    if s.count("оо") == 0:
        a.add(i)
        print(i)
print(len(a))
