import itertools
from itertools import repeat

a = set()
for i in itertools.product("рустам", repeat=6):
    s = "".join(i)
    ss = s.replace("р","с").replace("т", "с").replace("м","с")
    if ss.count("с") >= 3:
        a.add(i)
        print(i)
print(len(a))
