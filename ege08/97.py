import itertools

a = set()
for i in itertools.permutations("калий", r = 5):
    ss = "".join(i).replace("иак", "X")
    if i[0] != "й" and ss.count("X") ==0:
        a.add(i)
        print(i)
print(len(a))