import itertools

a = set()
for i in itertools.permutations("марта", r = 5):
    s = ''.join(i)
    ss = s.replace("аа", "x")
    if ss.count("x") == 0:
        a.add(i)
        print(i)
print(len(a))
