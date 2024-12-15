import itertools

a = set()
for i in itertools.permutations("кабинет", r = 7):
    ss = "".join(i).replace("еа", "X")
    if i[0] != "б" and ss.count("X") ==0:
        a.add(i)
        print(i)
print(len(a))