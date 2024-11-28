import itertools
from itertools import repeat

for i, s in enumerate(itertools.product("ВЕКНО", repeat=5), 1):
    if s.count("О") == 1 and s.count("Е") == 1:
        print(i, s)