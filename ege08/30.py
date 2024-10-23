import itertools
from itertools import repeat
k = 0
for i in itertools.product("ГОД", repeat = 6):
    if i[0] != "О" and i[-1] != "О":
        k += 1
print(k)