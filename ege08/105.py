import itertools

a = set()
for i in itertools.permutations("нобелий", r = 7):
    ss = "".join(i).replace("ийо", "X")
    if i[0] != "й" and ss.count("X") ==0:
        a.add(i)
        print(i)
print(len(a))