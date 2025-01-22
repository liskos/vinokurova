import itertools
from itertools import repeat

a = set()
for i in itertools.product("сакура", repeat= 6):
    s = "".join(i)
    if s.count("а") <= 1 and s.count("у") <= 1:
        a.add(i)
        print(i)
print(len(a))
