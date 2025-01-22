import itertools
from itertools import repeat

for n, i in enumerate(itertools.product("авдпр", repeat = 4), 1):
    s = "".join(i)
    print(n, i)
    