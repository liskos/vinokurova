import itertools

a = set()
for i in itertools.permutations("вентиль", r = 7):
    s = "".join(i)
    ss = s.replace("еьи", "x")
    ss = ss.replace("иье", "x")
    if i[-1] != "ь" and ss.count("x") == 0:
        a.add(i)
        print(i)
print(len(a))