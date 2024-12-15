import itertools

a = set()
for i in itertools.permutations("пайщик", r = 6):
    ss = "".join(i).replace("иа", "X")
    if i[0] != "й" and ss.count("X") ==0:
        a.add(i)
        print(i)
print(len(a))