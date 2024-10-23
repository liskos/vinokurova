import itertools
from itertools import repeat

for i, s in enumerate(itertools.product("АКРУ", repeat = 5), 1):
    if s[0] == "У" and s[1] == "К" and s[2] == "А" and s[3] == "Р" and s[4] == "А":
        print(i, s)
        break