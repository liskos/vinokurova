import itertools
from itertools import repeat
k = 0
for i in itertools.product("КУМА", repeat = 5):
    if i[0] == "К" or i[0] == "М" and i[-1] == "У" or i[-1] == "А":
        k += 1
print(k)