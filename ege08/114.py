import itertools

a = set()
for i in itertools.permutations("абак", r = 4):
    s = "".join(i)

    if i[0] != "ь" and ss.count("x") == 0:
        a.add(i)
        print(i)
print(len(a))