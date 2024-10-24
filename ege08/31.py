import itertools
from timeit import repeat
k = 0
for i in itertools.product("МЕТРО", repeat = 4):
    if i[0] in "МТР" and i[-1] in "ЕО":
        k += 1
print(k)