import itertools

a = set()
for i in itertools.permutations("ареал", r = 5):
    s = ''.join(i)
    ss = s.replace("е", "а")
    if ss.count("аа") == 0:
        a.add(i)
        print(i)
print(len(a))
