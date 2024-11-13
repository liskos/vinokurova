import itertools
from itertools import repeat

a = set()
for i in itertools.product("КУЛОН", repeat = 4):
    if i.count("У") >= 1:
        a.add(i)
print(len(a))