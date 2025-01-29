import itertools
from itertools import repeat

for i in itertools.product("лида", repeat=4):
    s = "".join(i)
    if s.count("и") <= 2 and s.count("а") <= 2 and