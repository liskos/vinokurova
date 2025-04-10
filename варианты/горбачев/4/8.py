import itertools

a = set()
for i in itertools.product("0123456", repeat = 7):
    s = "".join(i)
    if s[0] != "3" and s[0] != "5" and s[0] != "0" and s[-1] != "0" and s[-1] != "2" and s[-1] != "4" and s[-1] != "6" and s.count("0") <= 1:
        a.add(i)
print(len(a))