import itertools
from itertools import repeat

a = set()
for i in itertools.product("джобс", repeat = 6):
    s = "".join(i)
    if s.count("д") == 1 and s.count("о") == 1 and s.count("с") == 1 and s.count("ж") <=2:
        a.add(i)
        print(i)
print(len(a))
