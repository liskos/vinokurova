import itertools
from itertools import repeat

a = set()
for i in itertools.product("канкан", repeat=6):
    s = "".join(i)
    ss = s.replace("н","к")
    if ss.count("к") >= 3:
        a.add(i)
        print(i)
print(len(a))