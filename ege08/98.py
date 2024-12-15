import itertools

a = set()
for i in itertools.permutations("гелий", r = 5):
    ss = "".join(i).replace("ией", "X")
    if i[0] != "й" and ss.count("X") ==0:
        a.add(i)
        print(i)
print(len(a))