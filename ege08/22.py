import itertools
from itertools import repeat

k = 0
for i in itertools.product("КОТ", repeat= 5):
    if i.count("О") == 2:
        k += 1
print(k)