import itertools
from itertools import repeat

a = set()
for i in itertools.product("ABCDX", repeat = 4):
    if i.count("X") == 1:
        a.add(i)
print(len(a))