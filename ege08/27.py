import itertools
from itertools import repeat

k = 0
for i in itertools.product("КРОТ", repeat = 6):
    if i.count("О") == 1:
        k += 1
print(k)