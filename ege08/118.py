import itertools

a = set()
for i in itertools.permutations("аврора", r = 6):
    s = ''.join(i)
    ss = s.replace("аа", "x").replace("рр", "y")
    if ss.count("x") == 0 and ss.count("y") == 0:
        a.add(i)
        print(i)
print(len(a))
