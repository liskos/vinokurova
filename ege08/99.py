import itertools

a = set()
for i in itertools.permutations("ничья", r = 5):
    ss = "".join(i).replace("ьия", "X")
    if i[0] != "ь" and ss.count("X") ==0:
        a.add(i)
        print(i)
print(len(a))