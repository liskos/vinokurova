import itertools
from itertools import repeat

for i, s in enumerate(itertools.product("АКРУ", repeat = 5), 1):
    if s[0] == "К":
        print(i, s)
        break