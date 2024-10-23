import itertools
from itertools import repeat

k = 0
for i in itertools.product("МАРТ", repeat= 6):
    if i.count("Р") == 2:
        k += 1
print(k)