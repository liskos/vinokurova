import itertools
from itertools import repeat

for i, s in enumerate(itertools.product("АИОУЭ", repeat=4), 1):
    if s[0] == "И" and s[1] == "А" and s[2] == "А" and s[3] == "Э":
        print(i, s)