import itertools
from itertools import repeat

for i, s in enumerate(itertools.product("АВГДИНОР", repeat=4), 1):
    if s[0] == "Г" and s[1] == "О":
        print(i, s)