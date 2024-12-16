import itertools

a = set()
for i in itertools.permutations("клоун", r = 5):
    s = "".join(i)
    ss = s.replace("к", "б").replace("л", "б").replace("н","б")
    ss = ss.replace("о", "а").replace("у", "а")
    if "aa" not in ss and "бб" not in ss:
        a.add(i)
        print(i)
print(len(a))