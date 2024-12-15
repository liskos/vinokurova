import itertools

a = set()
for i in itertools.permutations("надпись", r = 7):
    ss = "".join(i).replace("ьиа", "X")
    if i[0] != "ь" and ss.count("X") ==0:
        a.add(i)
        print(i)
print(len(a))