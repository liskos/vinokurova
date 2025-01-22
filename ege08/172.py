import itertools
import shutil
from itertools import repeat

a = set()
for i in itertools.product("соловей", repeat=5):
    s = "".join(i)
    if s[0] != "й" and s[-1]!= "й" and "ей" not in s and "йе" not in s and s.count("й") <= 1:
        a.add(i)
        print(i)
print(len(a))