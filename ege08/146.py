import itertools
from itertools import repeat

a = set()
for i in itertools.product("размах", repeat=6):
    s = "".join(i)
    ss = s.replace("р","х").replace("з", "х").replace("м","х")
    if ss.count("х") >= 3:
        a.add(i)
        print(i)
print(len(a))