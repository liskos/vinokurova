import itertools
from itertools import repeat

a = set()
for i in itertools.product("радуга", repeat=6):
    s = "".join(i)
    ss = s.replace("р","с").replace("д", "с").replace("г","с")
    if ss.count("с") >= 3:
        a.add(i)
        print(i)
print(len(a))