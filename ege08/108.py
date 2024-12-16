import itertools

a = set()
for i in itertools.permutations("комета", r = 6):
    s = "".join(i)
    ss = s.replace("к", "б").replace("м","б").replace("т","б")
    ss = ss.replace("о", "а").replace("е", "а")
    if "aa" not in ss and "бб" not in ss:
        a.add(i)
        print(i)
print(len(a))