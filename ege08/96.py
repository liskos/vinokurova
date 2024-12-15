import itertools

a = set()
for i in itertools.permutations("комбайн", r = 7):
    ss = "".join(i).replace("ай", "X")
    if i[0] != "й" and ss.count("X") ==0:
        a.add(i)
        print(i)
print(len(a))