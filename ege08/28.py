import itertools
from itertools import repeat
k = 0
for i in itertools.product("КРАНТ", repeat = 5):
    if i.count("К") == 2:
        k += 1
print(k)