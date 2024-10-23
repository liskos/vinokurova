import itertools
from itertools import repeat

for i, s in enumerate(itertools.product("АКРУ", repeat = 5), 1):
    if s[0] == "Р" and s[1] == "У" and s[2] == "К" and s[3] == "А" and s[4] == "А":
        print(i, s)
        break