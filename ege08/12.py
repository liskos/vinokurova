import itertools
from itertools import repeat

for i, s in enumerate(itertools.product("АОУ", repeat = 5), 1):
    if s[0] == "О":
        print(i, s)
        break