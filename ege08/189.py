import itertools
from itertools import repeat

a = set()
for i in itertools.product("корнет", repeat= 5):
    s = "".join(i)
    if s.count("е") <= 1 and s.count("о") <= 1:
        a.add(i)
        print(i)
print(len(a))
