import itertools
from itertools import repeat

a = set()
for i in itertools.product("каркас", repeat=6):
    s = "".join(i)
    ss = s.replace("р","с").replace("к", "с")
    if ss.count("с") >= 3:
        a.add(i)
        print(i)
print(len(a))