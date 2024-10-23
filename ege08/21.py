import itertools
from itertools import repeat

k = 0
for i in itertools.product("ЛЕТО", repeat = 4):
    if i[0] == "Л" or i[0] == "Т":
        k += 1
print(k)