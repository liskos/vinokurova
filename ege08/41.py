import itertools
from itertools import repeat

a = set()
for i in itertools.product("КРАН", repeat = 3):
    if i.count("А") >= 1:
        a.add(i)
print(len(a))