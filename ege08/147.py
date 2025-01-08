import itertools
from itertools import repeat

a = set()
for i in itertools.product("кортик", repeat=6):
    s = "".join(i)
    ss = s.replace("к","с").replace("т", "с").replace("р","с")
    if ss.count("с") >= 3:
        a.add(i)
        print(i)
print(len(a))