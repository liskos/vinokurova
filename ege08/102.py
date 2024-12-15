import itertools

a = set()
for i in itertools.permutations("нигрол", r = 6):
    ss = "".join(i).replace("оиг", "X")
    if i[0] != "О" and ss.count("X") ==0:
        a.add(i)
        print(i)
print(len(a))