import itertools

a = set()
for i in itertools.permutations("здание", r = 6):
    s = ''.join(i)
    ss = s.replace("е", "а").replace("и", "а")
    if ss.count("аа") == 0:
        a.add(i)
        print(i)
print(len(a))
