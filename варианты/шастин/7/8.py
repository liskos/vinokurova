import itertools
from itertools import repeat

for i in itertools.product("дионсй",repeat=6):
    s = "".join(i)
    if (s.count("д")== 1 or s.count("н")==1) and "сс" not in s :

