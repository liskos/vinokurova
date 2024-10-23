import itertools
from itertools import repeat

for i, s in enumerate(itertools.product("АОУ", repeat = 5), 1):
    if s[0] == "О" and s[1] == "А" and s[2] == "О" and s[3] == "А":
        print(i, s)