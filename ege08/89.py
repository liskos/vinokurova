import itertools
from itertools import repeat
k = 0
for i in itertools.product("ггcс", repeat = 6):
    if i[0] == "г" and i[-1] == "с":
        k += 1
print(k)