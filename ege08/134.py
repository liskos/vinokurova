import itertools

a = set()
for i in itertools.permutations("ворота", r = 6):
    s = ''.join(i)
    ss = s.replace("о", "а")
    if ss.count("аа") == 0:
        a.add(i)
        print(i)
print(len(a))
