import itertools
from itertools import repeat

for i, s in enumerate(itertools.product("АКРУ", repeat = 5), 1):
    if i == 250:
        print(i, "".join(s))