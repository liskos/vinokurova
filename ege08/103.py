import itertools

a = set()
for i in itertools.permutations("купчиха", r = 7):
    ss = "".join(i).replace("иау", "X")
    if i[0] != "ч" and ss.count("X") ==0:
        a.add(i)
        print(i)
print(len(a))