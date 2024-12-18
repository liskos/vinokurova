import  itertools
from itertools import repeat

for i, s in enumerate(itertools.product("УОА", repeat = 5), 1):
    if i == 100:
        print(i, "".join(s))