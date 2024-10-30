import itertools
from itertools import repeat

a = set()
for i in itertools.product("ЛЮСТРА", repeat = 5):
    if i.count('Ю') <= 2 and i[-1] not in "ЛСТР":
        a.add(i)
print(len(a))