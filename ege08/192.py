import itertools
from itertools import repeat
k = 0
for i in itertools.product("марина", repeat = 8):
    s = "".join(i)
    if "мари" in s[:3] and s[0]!=s[1] and s[1]!=s[2] and s[2]!=s[3]:
        k += 1
        print(i)
        if s == "марианна":
            print(k, i)