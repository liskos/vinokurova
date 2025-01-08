import itertools
from itertools import repeat

for i,s in enumerate(itertools.product("АИОУЭ", repeat=6),1):
    a = "".join(s)
    if a[0]== "О" and a[-1]=="О":
        print(i, s)