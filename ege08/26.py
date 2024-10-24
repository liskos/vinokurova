import itertools
from itertools import repeat
k = 0
for i in itertools.product("КУМА", repeat = 5):
    if (i[0] in "КМ") and (i[-1] in "УА"):
        k += 1
print(k)