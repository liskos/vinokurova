import itertools
from itertools import repeat

for i, s in enumerate(itertools.product("ВЕКНО", repeat=5), 1):
    if s.count("Н") == 2 and s.count("К") == 2:
        print(i, s)