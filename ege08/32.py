import itertools
from itertools import repeat
k = 0
for i in itertools.product("ABCD", repeat = 3):
    i = "".join(i)
    if "BC" not in i and "CB" not in i:
        if i.count("A") == 0:
            k += 1
        elif i.count("A") == 1:
            if "AD" in i or "DA" in i:
                k += 1
        elif i.count("A") == 2:
            if i == "ADA":
                k += 1
print(k)