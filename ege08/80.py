import itertools
from itertools import repeat

for i, s in enumerate(itertools.product("АВГЕН", repeat=4), 1):
    if "А" not in s:
        print(i, s)