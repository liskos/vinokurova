import itertools

a = set()
for i in itertools.permutations('01234567', r = 6):
    s = "".join(i)
    if s[0] != "0" and "54" not in s and "26" in s:
        a.add(i)
print(len(a))