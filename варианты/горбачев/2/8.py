import itertools
from itertools import repeat

for i,s in enumerate(itertools.product("аикмнортф", repeat = 6), 1):
    ss = "".join(s)
    if ss[0] != "а" and ss.count("р") == 3 and "и" not in ss:
        print(i, s)