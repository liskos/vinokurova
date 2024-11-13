import itertools
from itertools import repeat

a = set()
for i in itertools.product("ABCX", repeat = 5):
    if i.count("X") == 1 and "X" in i[-1]:
        a.add(i)
    elif i.count("X") == 0:
        a.add(i)
print(len(a))