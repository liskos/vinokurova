import itertools
from itertools import repeat

for i, s in enumerate(itertools.product("АКРУ", repeat = 5), 1):
    print(i,"".join(s))