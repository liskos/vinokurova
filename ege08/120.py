import itertools

a = set()
for i in itertools.permutations("приказ", r = 4):
    s = ''.join(i)
    ss = s.replace("и", "а")
    if ss.count("а") == 1:
        a.add(i)
        print(i)
print(len(a))
