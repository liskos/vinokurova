import itertools

a = set()
for i in itertools.permutations("пескарь", r = 7):
    s = "".join(i)
    ss = s.replace("ье", "x")
    ss = ss.replace("ьа", "x")
    ss = ss.replace("ьр", "x")
    if i[0] != "ь" and ss.count("x") == 0:
        a.add(i)
        print(i)
print(len(a))