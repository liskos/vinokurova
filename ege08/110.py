import itertools

a = set()
for i in itertools.permutations("рулька", r = 6):
    s = "".join(i)
    ss = s.replace("уь", "x")
    ss = ss.replace("аь", "x")
    if i[0] != "ь" and ss.count("x") == 0:
        a.add(i)
        print(i)
print(len(a))