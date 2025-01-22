import itertools
from itertools import repeat

a = set()
for i in itertools.product("аклош", repeat=5):
    s = "".join(i)
    ss = s.replace("о","а")
    if ss.count("а") >= 1:
        a.add(i)
        print(i)
print(len(a))
    