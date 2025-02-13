import itertools
from itertools import repeat
k = 0
for i in itertools.product("дионсй",repeat=6):
    s = "".join(i)
    if (("д" in s) != ("н" in s)) and i[0] != i[1] and i[1] != i[2] and i[2] != i[3] and i[3] != i[4] and i[4]!=i[5]:
        k += 1
print(k)

