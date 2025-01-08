import itertools
from itertools import repeat

a = set()
for i in itertools.product("xywz", repeat=4):
    s = "".join(i)
    if s[0] != "x" and s[0] != s[2] and s[1]!=s[3]:
        a.add(i)
        print(i)
print(len(a))
