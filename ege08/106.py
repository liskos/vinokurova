import itertools

a = set()
for i in itertools.permutations("нода", r = 4):
    ss = "".join(i).replace("", "X")
    if i[0] != "О" and ss.count("X") ==0:
        a.add(i)
        print(i)
print(len(a))