import itertools
from itertools import repeat
k = 0
for i in itertools.product("ABCD", repeat = 3):
    if i.count("AD") == 1 or i.count("DA") == 1:
        k += 1
print(k)