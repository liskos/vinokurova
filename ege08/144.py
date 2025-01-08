import itertools
from itertools import repeat

a = set()
for i in itertools.product("азимут", repeat=6):
    s = "".join(i)
    ss = s.replace("м","з").replace("т", "з")
    if ss.count("з") >= 3:
        a.add(i)
        print(i)
print(len(a))