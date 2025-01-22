import itertools
from itertools import repeat

for n, i in enumerate(itertools.product("марина", repeat = 8), 1):
    s = "".join(i)
    if