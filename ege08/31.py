import itertools
from timeit import repeat
k = 0
for i in itertools.product("МЕТРО", repeat = 4):
    if i[0] != "Е" and i[0] != "О" and i[-1] =="Е" or i[-1] =="О":
        k += 1
print(k)