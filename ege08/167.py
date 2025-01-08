import itertools
from itertools import repeat

a = set()
for i in itertools.product("объем", repeat=4):
    s = "".join(i)
    if s.count("о") == 1 and s[0]!="ъ" and s[-1] !="ъ":
        a.add(i)
        print(i)
print(len(a))