import itertools

a = set()
for i in itertools.permutations("панель", r = 6):
    ss = "".join(i).replace("еап", "X")
    if i[0] != "ь" and ss.count("X") ==0:
        a.add(i)
        print(i)
print(len(a))