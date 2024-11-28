import itertools
from itertools import repeat

for i, s in enumerate(itertools.product("АГИЛМОРТ", repeat=4), 1):
    if s[2] == "А" and s[3] == "Л":
        print(i, s)
        