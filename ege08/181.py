import itertools

a = set()
for i in itertools.permutations("запись", r = 6):
    s = "".join(i)
    if s[0] != "ь" and "аь" not in s and "иь" not in s:
        a.add(i)
        print(i)
print(len(a))