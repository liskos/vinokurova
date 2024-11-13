import itertools
from itertools import repeat

for i, s in enumerate(itertools.product("АМРТ", repeat = 4), 1):
    print(i,"".join(s))