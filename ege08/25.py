import itertools
from itertools import repeat

k = 0
for i in itertools.product("ТОК", repeat= 6):
    if i[0] == "Т" or i[0] == "К":
        k += 1
print(k)