import itertools

a = set()
for i in itertools.permutations("МАНОК", r = 5):
    ss = "".join(i).replace("АО", "X")
    if i[0] != "О" and ss.count("X") ==0:
        a.add(i)
        print(i)
print(len(a))