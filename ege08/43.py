import itertools
from itertools import repeat

a = set()
for i in itertools.product("ЛЕТО", repeat = 5):
    if i.count("Е") >= 1:
        a.add(i)
print(len(a))