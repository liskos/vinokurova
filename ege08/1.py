import itertools
from itertools import repeat

for i, s in enumerate(itertools.product("АОУ", repeat = 5), 1):
    if i == 101:
        print(i, "".join(s))
