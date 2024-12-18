import itertools
from itertools import repeat

a = set()
for i in itertools.product("герой", repeat = 4):
    s = "".join(i)
    if i[0] != "й" and (i.count("е") != 0 or i.count("о") != 0):
        a.add(i)
        print(i)
print(len(a))
    