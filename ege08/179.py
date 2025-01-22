import itertools
from itertools import repeat

a = set()
for n, i in enumerate(itertools.product("щогба", repeat=6), 1):
    s = "".join(i)
    if s[0] == "о" and s[1] == "б" and s[2] == "щ" and s[3] == "а" and s[4] == "г" and s[5] == "а":
        print(n, i)