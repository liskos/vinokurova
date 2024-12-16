import itertools

a = set()
for i in itertools.permutations("абрикос", r = 7):
    s = "".join(i)
    ss = s.replace("к", "б").replace("р", "б").replace("с", "б")
    ss = ss.replace("о", "а").replace("и", "а")
    if "aa" not in ss and "бб" not in ss:
        a.add(i)
        print(i)
print(len(a))