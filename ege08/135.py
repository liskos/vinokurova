import itertools

a = set()
for i in itertools.permutations("кабала", r = 6):
    s = ''.join(i)
    if s.count("аа") == 0:
        a.add(i)
        print(i)
print(len(a))
