import itertools

a = set()
for i in itertools.permutations("айсберг", r = 7):
    s = "".join(i)
    ss = s.replace("йа", "x")
    ss = ss.replace("йе", "x")
    if i[0] != "й" and ss.count("x") == 0:
        a.add(i)
        print(i)
print(len(a))