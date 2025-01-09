import itertools

a = set()
for i in itertools.permutations("нигрол", r = 6):
    ss = "".join(i)
    if i[0] != "о" and "оиг" not in ss:
        a.add(i)
        print(i)
print(len(a))